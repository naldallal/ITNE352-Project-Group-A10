import socket
import tkinter as tk
from tkinter import messagebox, simpledialog

# Server IP & Port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

class NewsClient:
    def __init__(self, master):
        # main window in the app & title of it
        self.master = master
        self.master.title("News Client")

        # create client socket 
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

        # user will enter his name in the dialog box 
        self.username = simpledialog.askstring("Input", "Enter your name:")
        self.client_socket.sendall(self.username.encode('utf-8'))

        #Greeting 
        greeting = self.client_socket.recv(1024).decode('utf-8')
        self.show_message(greeting)

        # call the (creat_widgets ) method to setup the main menu
        self.create_widgets()

    # connect with the server 
    def connect_to_server(self):
        try:
            self.client_socket.connect((SERVER_IP, SERVER_PORT))

        except ConnectionRefusedError:
            messagebox.showerror("Connection Error", "Could not connect to server.")
            self.master.quit()

    # set up main menu interface
    def create_widgets(self):
        # creat frame for main menu & pack to control the placement and layout of widgets within a container
        self.main_menu = tk.Frame(self.master)
        self.main_menu.pack()
        self.label = tk.Label(self.main_menu, text="Main Menu")
        self.label.pack()

        # buttons for options in the main menu 
        self.search_button = tk.Button(self.main_menu, text="Search Headlines", command=self.search_headlines)
        self.search_button.pack()

        self.list_sources_button = tk.Button(self.main_menu, text="List of Sources", command=self.list_sources)
        self.list_sources_button.pack()

        self.quit_button = tk.Button(self.main_menu, text="Quit", command=self.quit)
        self.quit_button.pack()

     # method opens a new window for searching headlines
    def search_headlines(self):
        #top-level to open seperate window for " search headlines "
        self.headlines_window = tk.Toplevel(self.master)
        self.headlines_window.title("Search Headlines")

        self.label = tk.Label(self.headlines_window, text="Choose an option:")
        self.label.pack()
        
        # create button for parameters of search using headline 
        self.keyword_button = tk.Button(self.headlines_window, text="Search by Keyword", command=self.search_by_keyword)
        self.keyword_button.pack()

        self.category_button = tk.Button(self.headlines_window, text="Search by Category", command=self.search_by_category)
        self.category_button.pack()

        self.country_button = tk.Button(self.headlines_window, text="Search by Country", command=self.search_by_country)
        self.country_button.pack()

        self.list_all_button = tk.Button(self.headlines_window, text="List All Headlines", command=self.list_all_headlines)
        self.list_all_button.pack()

        self.back_button = tk.Button(self.headlines_window, text="Back to Main Menu", command=self.headlines_window.destroy)
        self.back_button.pack()

    # this method triggered when the user selects to search by keyword.
    def search_by_keyword(self):
        keyword = simpledialog.askstring("Input", "Enter the keyword:")
        self.client_socket.sendall(f"headline-keyword-{keyword}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_message(response)
    # method is triggered when the user selects to search by category.
    def search_by_category(self):
        category = simpledialog.askstring("Input", "Enter category [ business, general, health, science, sports, technology]:")
        self.client_socket.sendall(f"headline-category-{category}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_message(response)

    # method is triggered when the user selects to search by country.
    def search_by_country(self):
        country = simpledialog.askstring("Input", "Enter a country [au, ca, jp, ae, sa, kr, us, ma]:")
        self.client_socket.sendall(f"headline-country-{country}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_message(response)

    # method is triggered when the user selects show all headlines.
    def list_all_headlines(self):
        self.client_socket.sendall(b"headline-all")
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_message(response)

    # if user click second option it will open new window for list of source 
    def list_sources(self):
        self.sources_window = tk.Toplevel(self.master)
        self.sources_window.title("List of Sources")

        self.label = tk.Label(self.sources_window, text="Choose an option:")
        self.label.pack()
        # buttons for paramenters of source 
        self.category_button = tk.Button(self.sources_window, text="Search by Category", command=self.search_sources_by_category)
        self.category_button.pack()

        self.country_button = tk.Button(self.sources_window, text="Search by Country", command=self.search_sources_by_country)
        self.country_button.pack()

        self.language_button = tk.Button(self.sources_window, text="Search by Language", command=self.search_sources_by_language)
        self.language_button.pack()

        self.list_all_button = tk.Button(self.sources_window, text="List All", command=self.list_all_sources)
        self.list_all_button.pack()

        self.back_button = tk.Button(self.sources_window, text="Back to Main Menu", command=self.sources_window.destroy)
        self.back_button.pack()

    # method is triggered when the user selects search by source category.
    def search_sources_by_category(self):
        category = simpledialog.askstring("Input", "Enter category (business, general, health, science, sports, technology):")
        self.client_socket.sendall(f"source-category-{category}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_message(response)

    # method is triggered when the user selects search by source country.
    def search_sources_by_country(self):
        country = simpledialog.askstring("Input", "Enter country (au, ca, jp, ae, sa, kr, us, ma):")
        self.client_socket.sendall(f"source-country-{country}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_message(response)

    # method is triggered when the user selects search by source language 
    def search_sources_by_language(self):
        language = simpledialog.askstring("Input", "Enter language (ar, en):")
        self.client_socket.sendall(f"source-language-{language}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_message(response)

    def list_all_sources(self):
        self.client_socket.sendall(b"source-all")
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_message(response)

    # this method for displays a message box with the provided message
    def show_message(self, message):
        messagebox.showinfo("Response", message)
     
    # foe qoutting the app
    def quit(self):
        self.client_socket.sendall(b'Quit')
        self.client_socket.close()
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = NewsClient(root)
    root.mainloop()