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

# Main execution
root = tk.Tk()
root.title("News Client")
root.geometry("470x500")

# Create the main frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Ask for the username
username = simpledialog.askstring("Input", "Enter your name:")

# Main function to create the GUI
def create_widgets():
    # Clear the main frame first
    for widget in main_frame.winfo_children():
        widget.destroy()

    label = tk.Label(main_frame, text="Main Menu", font="Calibre 20 bold")
    label.pack(pady=10)

    search_button = tk.Button(main_frame, text="Search Headlines", command=search_headlines, font="Calibre 13 bold", padx=10, pady=10)
    search_button.pack(pady=10)

    list_sources_button = tk.Button(main_frame, text="List of Sources", command=list_sources, font="Calibre 13 bold", padx=10, pady=10)
    list_sources_button.pack(pady=10)

    quit_button = tk.Button(main_frame, text="Quit", command=quit_app, font="Calibre 13 bold", padx=10, pady=10)
    quit_button.pack(pady=10)

# Function to update the main frame with new content
def update_frame(content_func):
    for widget in main_frame.winfo_children():
        widget.destroy()
    content_func()

# Handle searching headlines
def search_headlines():
    update_frame(search_headlines_content)

def search_headlines_content():
    label = tk.Label(main_frame, text="Choose an option:", font="Calibre 13 bold", padx=10, pady=10)
    label.pack(pady=10)

    keyword_button = tk.Button(main_frame, text="Search by Keyword", command=search_by_keyword, font="Calibre 13 bold", padx=10, pady=10)
    keyword_button.pack(pady=10)

    category_button = tk.Button(main_frame, text="Search by Category", command=search_by_category, font="Calibre 13 bold", padx=10, pady=10)
    category_button.pack(pady=10)

    country_button = tk.Button(main_frame, text="Search by Country", command=search_by_country, font="Calibre 13 bold", padx=10, pady=10)
    country_button.pack(pady=10)

    list_all_button = tk.Button(main_frame, text="List All Headlines", command=list_all_headlines, font="Calibre 13 bold", padx=10, pady=10)
    list_all_button.pack(pady=10)

    back_button = tk.Button(main_frame, text="Back to Main Menu", command=create_widgets, font="Calibre 13 bold", padx=10, pady=10)
    back_button.pack(pady=10)

# Handle searching headlines by keyword
def search_by_keyword():
    keyword = simpledialog.askstring("Input", "Enter the keyword:")
    client_socket.sendall(f"headline-keyword-{keyword}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle searching headlines by category
def search_by_category():
    category = simpledialog.askstring("Input", "Enter category [ business, general, health, science, sports, technology ]:")
    client_socket.sendall(f"headline-category-{category}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle searching headlines by country
def search_by_country():
    country = simpledialog.askstring("Input", "Enter a country [au, ca, jp, ae, sa, kr, us, ma]:")
    client_socket.sendall(f"headline-country-{country}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle listing all headlines
def list_all_headlines():
    client_socket.sendall(b"headline-all")
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle listing sources
def list_sources():
    update_frame(list_sources_content)

def list_sources_content():
    label = tk.Label(main_frame, text="Choose an option:", font="Calibre 13 bold", padx=10, pady=10)
    label.pack(pady=10)

    category_button = tk.Button(main_frame, text="Search by Category", command=search_sources_by_category, font="Calibre 13 bold", padx=10, pady=10)
    category_button.pack(pady=10)

    country_button = tk.Button(main_frame, text="Search by Country", command=search_sources_by_country, font="Calibre 13 bold", padx=10, pady=10)
    country_button.pack(pady=10)

    language_button = tk.Button(main_frame, text="Search by Language", command=search_sources_by_language, font="Calibre 13 bold", padx=10, pady=10)
    language_button.pack(pady=10)

    list_all_button = tk.Button(main_frame, text="List All", command=list_all_sources, font="Calibre 13 bold", padx=10, pady=10)
    list_all_button.pack(pady=10)

    back_button = tk.Button(main_frame, text="Back to Main Menu", command=create_widgets, font="Calibre 13 bold", padx=10, pady=10)
    back_button.pack(pady=10)

# Handle searching sources by category
def search_sources_by_category():
    category = simpledialog.askstring("Input", "Enter category [ business, general, health, science, sports, technology ]:")
    client_socket.sendall(f"source-category-{category}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle searching sources by country
def search_sources_by_country():
    country = simpledialog.askstring("Input", "Enter country [ au, ca, jp, ae, sa, kr, us, ma ]:")
    client_socket.sendall(f"source-country-{country}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle searching sources by language
def search_sources_by_language():
    language = simpledialog.askstring("Input", "Enter language [ ar, en ]:")
    client_socket.sendall(f"source-language-{language}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle listing all sources
def list_all_sources():
    client_socket.sendall(b"source-all")
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle showing results
def show_results(response):
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    response_text = tk.Text(main_frame, height=15, width=50)
    response_text.pack()
    response_text.insert(tk.END, f"{response}\n")

    article_number = simpledialog.askstring("Input", "Enter the article number for details (or 'exit' to go back):")
    if article_number.lower() != 'exit':
        response_text.delete(1.0, tk.END)  # Clear the response before showing the article details
        client_socket.sendall(article_number.encode('utf-8'))
        article_details = client_socket.recv(4096).decode('utf-8')
        response_text.insert(tk.END, f"\nArticle Details: {article_details}\n")

    back_button = tk.Button(main_frame, text="Back to Main Menu", command=create_widgets, font="Calibre 13 bold", padx=10, pady=10)
    back_button.pack()

# Display message in a message box
def show_message(message):
    messagebox.showinfo("Response", message)

# Handle quitting the app
def quit_app():
    client_socket.sendall(b'quit')
    client_socket.close()
    root.quit()

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
