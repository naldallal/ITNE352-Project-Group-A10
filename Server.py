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
    main_menu = ["Search Headlines","List of Sources","Quit"]
    heading_menu = ["Search for keywords", "Search by category","Search by country", "List all new headlines", "Back to the main menu"]
    source_menu = ["Search by category","Search by country", "Search by language","List all", "Back to the main menu"]
    
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
