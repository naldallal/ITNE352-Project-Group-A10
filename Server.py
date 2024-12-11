from newsapi import NewsApiClient
import json
import socket
import threading
import os
import requests

# Function to handle client connections
def handle_client(client_socket):
    # Get the client's message
    name = client_socket.recv(1024).decode('utf-8')
    # print the client's name
    print(f"Connecting with: {name}")
    # Send a greeting message to the client
    client_socket.sendall(b"Hello, " + name.encode('utf-8'))
    # Specifying valid arguments
    Countries=["au", "ca", "jp", "ae", "sa", "kr", "us", "ma"]
    Languages=["ar", "en"]
    Categories=["business", "general", "health", "science", "sports", "technology"]
    # parameter in requesting news
    news = NewsApiClient(api_key='d9968ffc1e7f4b02b859492ab750f911')
    try:
        while True:
            valid = True
            # Get the client's request
            request = client_socket.recv(1024).decode('utf-8').lower()
            # print the client's request
            print(name,": requested",request)
            if request =="quit":
                client_socket.close()
                print("Client",name,"disconnected")
                return
            articles=[]
            # if the client requested the same request before then retreive answer from file
            if os.path.exists(name+'-'+request+'-A10'):
                # print("File found")   Debugging
                with open(name+'-'+request+'-A10', 'r') as json_file:
                    articles = json.load(json_file)
            else:
                # if the client did not request the same request before then retreive answer from API
                # print("No file found")
                # split the request into list
                requestList = request.split("-")
                # if we are requesting headlines
                if requestList[0] == "headline":
                    if requestList[1]=="keyword":
                        fetch=requests.get("https://newsapi.org/v2/top-headlines?q="+requestList[2]+"&apiKey=d9968ffc1e7f4b02b859492ab750f911")
                        response = fetch.json()
                        # print(response)   Debgging
                        # response = news.get_top_headlines(q=requestList[2])
                        # print(response)
                    elif requestList[1]=="category":
                        # if the category is not valid then return all headlines
                        if requestList[2] not in Categories:
                            response = news.get_top_headlines()
                            valid = False
                        else:
                            response = news.get_top_headlines(category=requestList[2])
                    elif requestList[1]=="country":
                        # if the country is not valid then return all headlines
                        if requestList[2] not in Countries:
                            response = news.get_top_headlines()
                            valid = False
                        else:
                            response = news.get_top_headlines(country=requestList[2])
                    elif requestList[1]=="all":
                        response = news.get_top_headlines()
                # if we are requesting sources
                elif requestList[0]=="source":
                    if requestList[1]=="category":
                        if requestList[2] not in Categories:
                            response = news.get_sources()
                            valid = False
                        else:
                            response = news.get_sources(category=requestList[2])
                    elif requestList[1]=="country":
                        if requestList[2] not in Countries:
                            response = news.get_sources()
                            valid = False
                        else:
                            response = news.get_sources(country=requestList[2])
                    elif requestList[1]=="language":
                        if requestList[2] not in Languages:
                            response = news.get_sources()
                            valid = False
                        else:
                            response = news.get_sources(language=requestList[2])
                    elif requestList[1]=="all":
                        response = news.get_sources()
                if response: # Extract relevant details and save them in a file 
                    if requestList[0]=="headline":
                        articles = response['articles'] 
                    elif requestList[0]=="source":
                        articles = response['sources']
                    articles = articles[:15]
                    fileName = name+'-'+request+'-A10'
                    with open(fileName, 'w') as json_file:
                            json.dump(articles, json_file, indent=4)
            if requestList[0]=="headline":
                # make a list of dictionaries of the articles
                articles_list = [ 
                        { "source_name": article['source']['name'], 
                        "author": article['author'], 
                        "title": article['title']
                        } for article in articles
                    ]
                # add more informations to be sent to the client
                if len(articles_list)==0:
                    articles_list.insert(0, {"validity": "No articles found"})
                if not valid:
                    articles_list.insert(0, {"validity": "Invalid argument, So returning all headlines"})
                client_socket.sendall(str(articles_list).encode('utf-8'))
                # wait for the client to send the number of the article he wants to see
                n=client_socket.recv(1024).decode('utf-8')
                # print(n)
                # if n=="quit":
                #     client_socket.close()
                #     print("Client",name,"disconnected")
                #     return
                if n.isdigit() and int(n)<=len(articles_list) and int(n)>0:
                    nn=int(n)-1
                    # prepare the article to be sent to the client
                    aspecified_article = {
                        "source_name": articles[nn]['source']['name'],
                        "author": articles[nn]['author'],
                        "title": articles[nn]['title'],
                        "URL": articles[nn]['url'],
                        "description": articles[nn]['description'],
                        "publish date": articles[nn]['publishedAt'].split("T")[0],
                        "publish time": articles[nn]['publishedAt'].split("T")[1].split("Z")[0],
                    }
                    client_socket.sendall(str(aspecified_article).encode('utf-8'))
                elif not n.isdigit() or int(n)>=len(articles_list) or  int(n)<0:
                    # handle letters and invalid numbers
                    client_socket.sendall(b"{\"validity\": \"Invalid article number\"}")
            elif requestList[0]=="source":
                # make a list of dictionaries of the sources
                sources_list = [ 
                        { "source_name": article['name'], 
                        } for article in articles
                    ]
                if len(sources_list)==0:
                    sources_list.insert(0, {"validity": "No sources found"})
                if not valid:
                    sources_list.insert(0, {"validity": "Invalid argument, So returning all sources"})
                client_socket.sendall(str(sources_list).encode('utf-8'))
                n=client_socket.recv(1024).decode('utf-8')
                # if n=="quit":
                #     client_socket.close()
                #     print("Client",name,"disconnected")
                #     return
                if n.isdigit() and int(n)<=len(sources_list) and int(n)>0:
                    nn=int(n)-1
                    # prepare the specified source to be sent to the client
                    aspecified_source = {
                        "source_name": articles[nn]['name'],
                        "country": articles[nn]['country'],
                        "description": articles[nn]['description'],
                        "URL": articles[nn]['url'],
                        "category": articles[nn]['category'],
                        "language": articles[nn]['language'],
                    }
                    client_socket.sendall(str(aspecified_source).encode('utf-8'))
                # handle letters and invalid numbers
                elif not n.isdigit() or int(n)>len(sources_list) or int(n)<=0:
                    client_socket.sendall(b"{\"validity\": \"Invalid source number\"}")
        client_socket.close()
        print("Client",name,"disconnected")
    except (ConnectionResetError, BrokenPipeError): 
        print(f"Client {name} disconnected unexpectedly") 
        client_socket.close() 
    except Exception as e: 
        print(f"An error occurred: {e}") 
        client_socket.close()
    finally:
        client_socket.close()
        # print("Client",name,"disconnected")

def start_server(server_ip, server_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"Listening on {server_ip}:{server_port}")
    
    active_connections = []

    while True:
        active_connections = [t for t in active_connections if t.is_alive()]

        if len(active_connections) < 3:
            client_socket, addr = server.accept()
            # Print that the client has connected
            # print(f"Accepted connection from {addr[0]}:{addr[1]}")
            
            # Create a new thread to handle the client
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
            
            # Append the thread to the active connections list
            active_connections.append(client_handler)
            
            # Remove finished threads from the active connections list
            active_connections = [t for t in active_connections if t.is_alive()]

if __name__ == "__main__":
    start_server("127.0.0.1", 9999)

# Main server function
# def start_server(server_ip, server_port):
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind((server_ip, server_port))
#     server.listen(5)
#     print(f"[*] Listening on {server_ip}:{server_port}")
 
#     while True:
#         client_socket, addr = server.accept()
#         # print that the client has connected
#         print(f"Accepted connection from {addr[0]}:{addr[1]}")
        
#         # Create a new thread to handle the client
#         client_handler = threading.Thread(target=handle_client, args=(client_socket,))
#         client_handler.start()
 
# if __name__ == "__main__":
#     start_server("127.0.0.1", 9999)