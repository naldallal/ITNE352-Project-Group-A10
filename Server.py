from newsapi import NewsApiClient
import json
import socket
import threading
import os

# Function to handle client connections
def handle_client(client_socket):
    # client_socket.send(b'Hello, Client!\nWhat is your name?')
    # Get the client's message
    name = client_socket.recv(1024).decode('utf-8')
    # print the client's name
    print(f"Connecting with: {name}")
    # Send a greeting message to the client
    client_socket.sendall(b"Hello, " + name.encode('utf-8'))
    Countries=["au", "ca", "jp", "ae", "sa", "kr", "us", "ma"]
    Languages=["ar", "en"]
    Categories=["business", "general", "health", "science", "sports", "technology"]
    while 5:
        valid = True
        news = NewsApiClient(api_key='d9968ffc1e7f4b02b859492ab750f911')
        request = client_socket.recv(1024).decode('utf-8').lower()
        if request =="quit":
            client_socket.close()
            print("Client",name,"disconnected")
            return
        articles=[]
        if os.path.exists(name+'-'+request+'-A10'):
            print("File found")
            with open(name+'-'+request+'-A10', 'r') as json_file:
                articles = json.load(json_file)
        else:
            print("No file found")
            requestList = request.split("-")
            if requestList[0] == "headline":
                if requestList[1]=="keyword":
                    response = news.get_top_headlines(q=requestList[2])
                elif requestList[1]=="category":
                    if requestList[2] not in Categories:
                        response = news.get_top_headlines()
                        valid = False
                    else:
                        response = news.get_top_headlines(category=requestList[2])
                elif requestList[1]=="country":
                    if requestList[2] not in Countries:
                        response = news.get_top_headlines()
                        valid = False
                    else:
                        response = news.get_top_headlines(country=requestList[2])
                elif requestList[1]=="all":
                    response = news.get_top_headlines()
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
            if response: # Extract relevant details and create a list of dictionaries 
                if requestList[0]=="headline":
                    articles = response['articles'] 
                    articles = articles[:15]
                    fileName = name+'-'+request+'-A10'
                elif requestList[0]=="source":
                    articles = response['sources']
                    articles = articles[:15]
                    fileName = name+'-'+request+'-A10'
            with open(fileName, 'w') as json_file:
                    json.dump(articles, json_file, indent=4)
        if requestList[0]=="headline":
            articles_list = [ 
                    { "source_name": article['source']['name'], 
                    "author": article['author'], 
                    "title": article['title']
                    } for article in articles
                ]
            if not valid:
                articles_list.insert(0, {"validity": "Invalid argument, So returning all headlines"})
            client_socket.sendall(str(articles_list).encode('utf-8'))
            n=client_socket.recv(1024).decode('utf-8')
            if n=="exit":
                continue
            elif n=="quit":
                client_socket.close()
                print("Client",name,"disconnected")
                return
            elif int(n)<len(articles_list) and int(n)>=0:
                nn=int(n)-2
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
            elif int(n)>=len(articles_list) or  int(n)<0:
                client_socket.sendall(b"Invalid article number")
        elif requestList[0]=="source":
            articles_list = [ 
                    { "source_name": article['name'], 
                    } for article in articles
                ]
            if not valid:
                articles_list.insert(0, {"validity": "Invalid argument, So returning all sources"})
            client_socket.sendall(str(articles_list).encode('utf-8'))
            n=client_socket.recv(1024).decode('utf-8')
            if n=="exit":
                continue
            elif n=="quit":
                client_socket.close()
                print("Client",name,"disconnected")
                return
            elif int(n)<=len(articles_list) and int(n)>0:
                nn=int(n)-1
                aspecified_article = {
                    "source_name": articles[nn]['name'],
                    "country": articles[nn]['country'],
                    "description": articles[nn]['description'],
                    "URL": articles[nn]['url'],
                    "category": articles[nn]['category'],
                    "language": articles[nn]['language'],
                }
                client_socket.sendall(str(aspecified_article).encode('utf-8'))
            elif int(n)>len(articles_list) or int(n)<=0:
                client_socket.sendall(b"Invalid article number")
    client_socket.close()
    print("Client",name,"disconnected")

 
# Main server function
def start_server(server_ip, server_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"[*] Listening on {server_ip}:{server_port}")
 
    while True:
        client_socket, addr = server.accept()
        # print that the client has connected
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        
        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
 
if __name__ == "__main__":
    start_server("127.0.0.1", 9999)