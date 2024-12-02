import socket

# Define server settings //check true???
SERVER_IP = '127.0.0.1'
SERVER_PORT = 65432

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # Get the client's name
    name = input("Enter your name: ")
    client_socket.sendall(name.encode('utf-8'))

    # Receive greeting from server
    greeting = client_socket.recv(1024).decode('utf-8')
    print(greeting)

    while True:
        # Display the main menu
        print("\n Main Menu:")
        print("A. Search Headlines")
        print("B. List of Sources")
        print("C. Quit")
        
        choice = input("Choose an option (1-3): ")

        if choice == 'A':
            search_headlines(client_socket)
        elif choice == 'B':
            list_sources(client_socket)
        elif choice == 'C':
            print("Quitting...")
            client_socket.sendall(b'Quit')
            break
        else:
            print("Invalid option, please try again !")

    client_socket.close()

def search_headlines(client_socket):
    while True:
        print("\n Search Headlines Menu:")
        print("A. Search for keywords")
        print("B. Search by category")
        print("C. Search by country")
        print("D. List all new headlines")
        print("E. Back to the main menu")
        
        choice = input("Choose an option (A-E)): ")

        if choice in ['A', 'B', 'C', 'D']:
            parameter = input("Enter your search parameter: ")
            client_socket.sendall(f"Search:{choice}:{parameter}".encode('utf-8'))

            # results handling
            response = client_socket.recv(1024).decode('utf-8')
            print("Response from server:", response)

     #----------------------------------------------------------------------------------------
        elif choice == 'E':
            break
        else:
            print("Invalid option, please try again.")

def list_sources(client_socket):
    while True:
        print("\n List of Sources Menu:")
        print("A. Search by category")
        print("B. Search by country")
        print("C. Search by language")
        print("D. List all")
        print("F. Back to the main menu")
        
        choice = input("Choose an option (A-F): ")

        if choice in ['A', 'B', 'C', 'D']:
            parameter = input("Enter your search parameter: ")
            client_socket.sendall(f"Source:{choice}:{parameter}".encode('utf-8'))
            # implement results handling 
            response = client_socket.recv(1024).decode('utf-8')
            print("Response from server:", response)
            #---------------------------------------------------------------------------------
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()