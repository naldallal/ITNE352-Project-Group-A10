import socket
import json

def connect_to_server(server_ip, server_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    
    name = input("Enter your name: ")
    client.send(name.encode('utf-8'))
    greeting = client.recv(1024).decode('utf-8')
    print(greeting)

    while True:
        request_type = input("Enter request type (headline/source): ")
        request_detail = input("Enter detail type (keyword/category/country/all): ")
        if request_detail != "all":
            request_value = input("Enter value for detail: ")
            request = f"{request_type}-{request_detail}-{request_value}"
        else:
            request = f"{request_type}-{request_detail}"

        client.send(request.encode('utf-8'))
        response = client.recv(4096).decode('utf-8')
        print(f"Response: {response}")

        client.send('5'.encode('utf-8'))
        
        if input("Do you want to make another request? (yes/no): ").lower() != 'yes':
            client.send('quit'.encode('utf-8'))
            break
    
    client.close()

if __name__ == "__main__":
    server_ip = "127.0.0.1"  # Adjust the IP address if needed
    server_port = 9999
    connect_to_server(server_ip, server_port)
