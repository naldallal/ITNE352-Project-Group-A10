import socket
import tkinter as tk
from tkinter import messagebox, simpledialog

# Server IP & Port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

class NewsClient:
    def __init__(self, master):
        self.master = master
        self.master.title("News Client")

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_server()

        self.username = simpledialog.askstring("Input", "Enter your name:")
        self.client_socket.sendall(self.username.encode('utf-8'))

        greeting = self.client_socket.recv(1024).decode('utf-8')
        self.show_message(greeting)

        self.create_widgets()

    def connect_to_server(self):
        try:
            self.client_socket.connect((SERVER_IP, SERVER_PORT))
        except ConnectionRefusedError:
            messagebox.showerror("Connection Error", "Could not connect to server.")
            self.master.quit()

    def create_widgets(self):
        self.main_menu = tk.Frame(self.master)
        self.main_menu.pack()
        self.label = tk.Label(self.main_menu, text="Main Menu")
        self.label.pack()

        self.search_button = tk.Button(self.main_menu, text="Search Headlines", command=self.search_headlines)
        self.search_button.pack()

        self.list_sources_button = tk.Button(self.main_menu, text="List of Sources", command=self.list_sources)
        self.list_sources_button.pack()

        self.quit_button = tk.Button(self.main_menu, text="Quit", command=self.quit)
        self.quit_button.pack()

    def search_headlines(self):
        self.headlines_window = tk.Toplevel(self.master)
        self.headlines_window.title("Search Headlines")

        self.label = tk.Label(self.headlines_window, text="Choose an option:")
        self.label.pack()

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

    def search_by_keyword(self):
        keyword = simpledialog.askstring("Input", "Enter the keyword:")
        self.client_socket.sendall(f"headline-keyword-{keyword}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_results(response, "headline")

    def search_by_category(self):
        category = simpledialog.askstring("Input", "Enter category [business, general, health, science, sports, technology]:")
        self.client_socket.sendall(f"headline-category-{category}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_results(response, "headline")

    def search_by_country(self):
        country = simpledialog.askstring("Input", "Enter a country [au, ca, jp, ae, sa, kr, us, ma]:")
        self.client_socket.sendall(f"headline-country-{country}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_results(response, "headline")

    def list_all_headlines(self):
        self.client_socket.sendall(b"headline-all")
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_results(response, "headline")

    def list_sources(self):
        self.sources_window = tk.Toplevel(self.master)
        self.sources_window.title("List of Sources")

        self.label = tk.Label(self.sources_window, text="Choose an option:")
        self.label.pack()

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

    def search_sources_by_category(self):
        category = simpledialog.askstring("Input", "Enter category (business, general, health, science, sports, technology):")
        self.client_socket.sendall(f"source-category-{category}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_results(response, "source")

    def search_sources_by_country(self):
        country = simpledialog.askstring("Input", "Enter country (au, ca, jp, ae, sa, kr, us, ma):")
        self.client_socket.sendall(f"source-country-{country}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_results(response, "source")

    def search_sources_by_language(self):
        language = simpledialog.askstring("Input", "Enter language (ar, en):")
        self.client_socket.sendall(f"source-language-{language}".encode('utf-8'))
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_results(response, "source")

    def list_all_sources(self):
        self.client_socket.sendall(b"source-all")
        response = self.client_socket.recv(4096).decode('utf-8')
        self.show_results(response, "source")

    def show_results(self, response, result_type):
        results = response.split('\n')
        self.results_window = tk.Toplevel(self.master)
        self.results_window.title("Results")

        self.label = tk.Label(self.results_window, text="Select an item for more details:")
        self.label.pack()

        self.listbox = tk.Listbox(self.results_window)
        for result in results:
            self.listbox.insert(tk.END, result)
        self.listbox.pack()

        self.details_button = tk.Button(self.results_window, text="Get Details", command=lambda: self.get_details(result_type))
        self.details_button.pack()

        self.back_button = tk.Button(self.results_window, text="Back to Main Menu", command=self.results_window.destroy)
        self.back_button.pack()

    def get_details(self, result_type):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.listbox.get(selected_index)
            self.client_socket.sendall(f"{result_type}-details-{selected_item}".encode('utf-8'))
            response = self.client_socket.recv(4096).decode('utf-8')
            self.show_message(response)
        else:
            messagebox.showwarning("Selection Error", "Please select an item from the list.")

    def show_message(self, message):
        messagebox.showinfo("Response", message)

    def quit(self):
        self.client_socket.sendall(b'Quit')
        self.client_socket.close()
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = NewsClient(root)
    root.mainloop()