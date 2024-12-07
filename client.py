import socket
import tkinter as tk
from tkinter import messagebox, simpledialog

# Server IP & Port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
def connect_to_server():
    client_socket.connect((SERVER_IP, SERVER_PORT))

# Display message in a message box
def show_message(message):
    messagebox.showinfo("Response", message)

# Handle quitting the app
def quit_app():
    client_socket.sendall(b'Quit')
    client_socket.close()
    root.quit()

# Handle searching headlines by keyword
def search_by_keyword():
    keyword = simpledialog.askstring("Input", "Enter the keyword:")
    client_socket.sendall(f"headline-keyword-{keyword}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)
    show_results(response)

# Handle searching headlines by category
def search_by_category():
    category = simpledialog.askstring("Input", "Enter category [ business, general, health, science, sports, technology ]:")
    client_socket.sendall(f"headline-category-{category}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)
    show_results(response)

# Handle searching headlines by country
def search_by_country():
    country = simpledialog.askstring("Input", "Enter a country [au, ca, jp, ae, sa, kr, us, ma]:")
    client_socket.sendall(f"headline-country-{country}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)
    show_results(response)

# Handle listing all headlines
def list_all_headlines():
    client_socket.sendall(b"headline-all")
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)
    show_results(response)

# Handle opening a window for searching headlines
def search_headlines():
    headlines_window = tk.Toplevel(root)
    headlines_window.title("Search Headlines")
    
    label = tk.Label(headlines_window, text="Choose an option:")
    label.pack()

    keyword_button = tk.Button(headlines_window, text="Search by Keyword", command=search_by_keyword)
    keyword_button.pack()

    category_button = tk.Button(headlines_window, text="Search by Category", command=search_by_category)
    category_button.pack()

    country_button = tk.Button(headlines_window, text="Search by Country", command=search_by_country)
    country_button.pack()

    list_all_button = tk.Button(headlines_window, text="List All Headlines", command=list_all_headlines)
    list_all_button.pack()

    back_button = tk.Button(headlines_window, text="Back to Main Menu", command=headlines_window.destroy)
    back_button.pack()

# Handle listing sources
def list_sources():
    sources_window = tk.Toplevel(root)
    sources_window.title("List of Sources")
    
    label = tk.Label(sources_window, text="Choose an option:")
    label.pack()

    category_button = tk.Button(sources_window, text="Search by Category", command=search_sources_by_category)
    category_button.pack()

    country_button = tk.Button(sources_window, text="Search by Country", command=search_sources_by_country)
    country_button.pack()

    language_button = tk.Button(sources_window, text="Search by Language", command=search_sources_by_language)
    language_button.pack()

    list_all_button = tk.Button(sources_window, text="List All", command=list_all_sources)
    list_all_button.pack()

    back_button = tk.Button(sources_window, text="Back to Main Menu", command=sources_window.destroy)
    back_button.pack()

# Handle searching sources by category
def search_sources_by_category():
    category = simpledialog.askstring("Input", "Enter category [ business, general, health, science, sports, technology ]:")
    client_socket.sendall(f"source-category-{category}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)
    show_results(response)

# Handle searching sources by country
def search_sources_by_country():
    country = simpledialog.askstring("Input", "Enter country [ au, ca, jp, ae, sa, kr, us, ma ]:")
    client_socket.sendall(f"source-country-{country}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)
    show_results(response)

# Handle searching sources by language
def search_sources_by_language():
    language = simpledialog.askstring("Input", "Enter language [ ar, en ]:")
    client_socket.sendall(f"source-language-{language}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)
    show_results(response)

# Handle listing all sources
def list_all_sources():
    client_socket.sendall(b"source-all")
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)
    show_results(response)

# Handle showing results
def show_results(response):
    results = response.split('\n')
    results_window = tk.Toplevel(root)
    results_window.title("Results")

    num_topic = simpledialog.askfloat("Input", "Select number of topics you are interested in for more details:")

    # Convert the float to an integer
    num_topic = int(num_topic)

    client_socket.sendall(str(num_topic).encode())
    response = client_socket.recv(4096).decode('utf-8')
    show_message(response)

    back_button = tk.Button(results_window, text="Back to Main Menu", command=results_window.destroy)
    back_button.pack()

# Main function to create the GUI
def create_widgets():
    # Create the main menu
    main_menu = tk.Frame(root)
    main_menu.pack()

    label = tk.Label(main_menu, text="Main Menu")
    label.pack()

    search_button = tk.Button(main_menu, text="Search Headlines", command=search_headlines)
    search_button.pack()

    list_sources_button = tk.Button(main_menu, text="List of Sources", command=list_sources)
    list_sources_button.pack()

    quit_button = tk.Button(main_menu, text="Quit", command=quit_app)
    quit_button.pack()

# Main execution
root = tk.Tk()
root.title("News Client")

# Ask for the username
username = simpledialog.askstring("Input", "Enter your name:")

# Connect to the server
connect_to_server()

# Send username to the server
client_socket.sendall(username.encode('utf-8'))

# Receive and show greeting message from the server
greeting = client_socket.recv(1024).decode('utf-8')
show_message(greeting)

# Set up the main menu
create_widgets()

# Run the Tkinter event loop
root.mainloop()
