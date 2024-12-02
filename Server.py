from newsapi import NewsApiClient

import socket
import threading

# Function to handle client connections
def handle_client(client_socket):
    from time import sleep
    # client_socket.send(b'Hello, Client!\nWhat is your name?')
    # Get the client's message
    name = client_socket.recv(1024).decode('utf-8')
    print(f"Connecting with: {name}")
    client_socket.sendall(b"Hello, " + name.encode('utf-8'))
    while True:
        news = NewsApiClient(api_key='669044070939452b80060306171002d9')
        request = client_socket.recv(1024).decode('utf-8')
        requestList = request.split("-")
        if requestList[0] == "headline":
            if requestList[1]=="keyword":
                response = news.get_top_headlines(q=requestList[2])
            elif requestList[1]=="category":
                response = news.get_top_headlines(category=requestList[2])
            elif requestList[1]=="country":
                response = news.get_top_headlines(country=requestList[2])
            elif requestList[1]=="all":
               response = news.get_top_headlines()
        elif requestList[0]=="source":
            if requestList[1]=="category":
                response = news.get_sources(category=requestList[2])
            elif requestList[1]=="country":
                response = news.get_sources(country=requestList[2])
            elif requestList[1]=="language":
                response = news.get_sources(language=requestList[2])
            elif requestList[1]=="all":
               response = news.get_sources()
    print(response)
            


        
        
        

    client_socket.close()

# Main server function
def start_server(server_ip, server_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"[*] Listening on {server_ip}:{server_port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        
        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server("0.0.0.0", 9999)
