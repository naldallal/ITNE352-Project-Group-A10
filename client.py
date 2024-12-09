import tkinter as tk
from tkinter import simpledialog
import ast

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, prompt=None):
        self.prompt = prompt
        self.result = None
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text=self.prompt).pack(pady=10)
        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)
        return self.entry

    def buttonbox(self):
        box = tk.Frame(self)
        submit_button = tk.Button(box, text="Submit", width=10, command=self.ok, default=tk.ACTIVE)
        submit_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)  # Submit on Enter key press
        box.pack()

    def apply(self):
        self.result = self.entry.get()

import socket
import tkinter as tk
from tkinter import messagebox

# Server IP & Port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
def connect_to_server():
    client_socket.connect((SERVER_IP, SERVER_PORT))
# Connect to the server
connect_to_server()

# Main execution
root = tk.Tk()
root.title("News Client")
root.geometry("500x600")

# Override the close button
def disable_close():
    pass  # You can also show a messagebox or do something else here if needed.

root.protocol("WM_DELETE_WINDOW", disable_close)

# Ask for the username using Custom Dialog
username = CustomDialog(root, title="Input", prompt="Enter your name:").result
# Send username to the server
client_socket.sendall(username.encode('utf-8'))

# Receive and show greeting message from the server
greeting = client_socket.recv(1024).decode('utf-8')

# Create the main frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

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

# searching headlines
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
    keyword = CustomDialog(root, title="Input", prompt="Enter the keyword:").result
    keyword = CustomDialog(root, title="Input", prompt="Enter the keyword:").result
    client_socket.sendall(f"headline-keyword-{keyword}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle searching headlines by category
def search_by_category():
    category = CustomDialog(root, title="Input", prompt="Enter category [ business, general, health, science, sports, technology ]:").result
    category = CustomDialog(root, title="Input", prompt="Enter category [ business, general, health, science, sports, technology ]:").result
    client_socket.sendall(f"headline-category-{category}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle searching headlines by country
def search_by_country():
    country = CustomDialog(root, title="Input", prompt="Enter a country [au, ca, jp, ae, sa, kr, us, ma]:").result
    country = CustomDialog(root, title="Input", prompt="Enter a country [au, ca, jp, ae, sa, kr, us, ma]:").result
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
    category = CustomDialog(root, title="Input", prompt="Enter category [ business, general, health, science, sports, technology ]:").result
    category = CustomDialog(root, title="Input", prompt="Enter category [ business, general, health, science, sports, technology ]:").result
    client_socket.sendall(f"source-category-{category}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle searching sources by country
def search_sources_by_country():
    country = CustomDialog(root, title="Input", prompt="Enter country [ au, ca, jp, ae, sa, kr, us, ma ]:").result
    country = CustomDialog(root, title="Input", prompt="Enter country [ au, ca, jp, ae, sa, kr, us, ma ]:").result
    client_socket.sendall(f"source-country-{country}".encode('utf-8'))
    response = client_socket.recv(4096).decode('utf-8')
    show_results(response)

# Handle searching sources by language
def search_sources_by_language():
    language = CustomDialog(root, title="Input", prompt="Enter language [ ar, en ]:").result
    language = CustomDialog(root, title="Input", prompt="Enter language [ ar, en ]:").result
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
    print(response)
    print(len(response))
    if len(response) == 16:
        response = response[1:]
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    response_text = tk.Text(main_frame, height=20, width=60, bg='#f5f5dc', fg='#8b4513')
    response_text.pack(pady=10)

    response_text.insert(tk.END, "Results:\n\n")

    # Assuming `response` is a string representation of a list of
    # Assuming `response` is a string representation of a list of
    # Assuming `response` is a string representation of a list of dictionaries
    try:
        data = ast.literal_eval(response)
        print("Data loaded successfully")  # Debug print
    except (ValueError, SyntaxError) as e:
        print(f"Error decoding string: {e}")  # Debug print
        response_text.insert(tk.END, f"Error decoding response: {e}")
        return

    if data: 
        validity_check = data[0] 
        if 'validity' in validity_check: 
            response_text.insert(tk.END, f"{validity_check['validity']}\n") 
            data = data[1:]  # Skip the first dictionary

    for idx, item in enumerate(data):
        response_text.insert(tk.END, f"{idx + 1}. ")
        for key, value in item.items():
            response_text.insert(tk.END, f"{key}: {value}\n")
        response_text.insert(tk.END, "\n")

    # Custom dialog box for entering article number
    def get_article_number():
        dialog = tk.Toplevel(root)
        dialog.title("Enter Article Number")
        dialog.geometry("300x150")

        label = tk.Label(dialog, text="Enter the article number for details:")
        label.pack(pady=10)

        entry = tk.Entry(dialog)
        entry.pack(pady=10)

        def submit():
            article_number = entry.get()
            dialog.destroy()
            #if article_number.lower() != 'exit':
            response_text.delete(1.0, tk.END)  # Clear the response before showing the article details
            client_socket.sendall(article_number.encode('utf-8'))
            article_details = client_socket.recv(4096).decode('utf-8')
            try:
                data = ast.literal_eval(article_details)
                print("Data loaded successfully")  # Debug print
                print(data)  # Debug print
            except (ValueError, SyntaxError) as e:
                print(f"Error decoding string: {e}")  # Debug print
            for key, value in data.items():
                response_text.insert(tk.END, f"{key}: {value}\n")
            response_text.insert(tk.END, "\n")
            # return response_text.insert(tk.END, f"\nArticle Details: {data}\n")


        submit_button = tk.Button(dialog, text="Submit", command=submit)
        submit_button.pack(pady=10)

    get_article_number()

    back_button = tk.Button(main_frame, text="Back to Main Menu", command=create_widgets, font="Calibre 13 bold", padx=10, pady=10, bg='#f5f5dc', fg='#8b4513', activebackground='#d2b48c')
    back_button.pack(pady=10)

# Handle quitting the app
def quit_app():
    client_socket.sendall(b'quit')
    client_socket.close()
    root.quit()

# Display message in a message box
def show_message(message):
    messagebox.showinfo("Response", message)
show_message(greeting)    

# Set up the main menu
create_widgets()
root.mainloop()

