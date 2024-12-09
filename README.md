# Multithreading-News-Information-System
## Project Description
This project is a multithreaded news information system that allows users to search for news from https://newsapi.org articles based headlines or sources and by specifying (keyword, country, category, ..). The system connect users to threads and handle three users at time. where tgey coonect with the server in a GUI interface.
  graphical user interface (GUI).
## Semester
First semester 2023-2024
## Group
Group: A10 \
Course code: ITNE352  
Section: 1 \
Student name - ID: Noor Zaher Aldallal - 202210337 \
Student name - ID: Noor Shafeeq Ashoor - 202210100 
## Table of Contents
+ README.md
+ Server.py
+ Client.py
+ JSON files
## Requirements
Ensure that you have Python installed on your system. \
Install newsapi module by running the following command: \
- pip install newsapi-python \
Ensure that you have the required libraries and modules:
- json
- socket
- threading
- os
- tkinter
- ast
## How to Run
1. Run the server.py file on the server machine.
2. Run the client.py file on the client machine.
3. Follow the instructions on the client interface to search for news articles.
## client-server scripts 
### Client scripts
#### Main functionalities: 
- connect to server.

- send the user name to the server .

- receives and displays the server's response.

- View article details.

- Quit the application.

#### Utilized packeges:
- socket, allows the client to connect to a server and send/receive data over a network.

- tkinter, create the graphical user interface (GUI) .

- tkinter.simpledialog , messagebox Provides a way to create simple dialog boxes and display message boxes to the user.

- ast, provide safely evaluate strings containing in Python literals (like lists or dictionaries) 


#### Functions and Classes: 
- connect_to_server function, establishes a connection to the server using the specified IP address and port.

- create_widgets function, set up the main menu of the application, and create buttons for different functionalities .

- update_frame function, clear the current content of the main frame and calls a specified function to populate it with new content.


- search_headlines function, update the interface to allow the user to choose options for searching headlines.

- search_headlines_content function, display the options for searching headlines by keyword, category, country, or listing all headlines.

- for each category parameter in search by headline we create function (search_by_keyword / search_by_category / search_by_country / list_all_headlines ) to take input from user, then send it to server for processing .

- list_sources function, update the main frame to show options for listing news sources.

- list_sources_content function ,display the options for searching sources by category, country, language, or listing all sources.

- for each category in list by sources we create function (source_by_category / source_by_country / source_by_language / list_all_sources ) to take input from user, then send it to the server to process it.

- show_results function, display the results received from the server in the main frame, including handling the response data and providing details for selected articles.

- get_article_number function, create a dialog for the user to input an article number to fetch detailed information about a specific article.

- show_message function, display an informational message box with the specified message.

- quit function, send a quit signal to the server, closes the socket connection, and exits the application.

### Server scripts
#### Main functionality:

- listens for incoming client connections.

- accept clients and put them in threat , then send greeting with client name.

- processes client requests.  /
if the request requested for the first time, the result will be fetched from API and save it in json file.  /
if the request requested for the second time, the result will be fetched from json file.

- Sends responses back to the clients.

- Handles client disconnections.

#### Utilized packeges

 - NewsApiClient, import NewsApiClient class from the newsapi library.

- socket, create and manage socket connections for communication between the server and clients.

- threading, allow server to handle multiple clients concurrently  by creating a new thread for each client connection.

- json, create json file.

- os, make sure if file available or need API request.

#### Functions and Classes: 
- handle_client function, handles communication with a connected client in the threat ( handles receiving requests -> processing them -> fetching news data -> and sending responses back to the client.). 

- start_server, initializes and runs the server and listen for incoming connections.

- __main__ block , the entry point of the application that calls the start_server function with predefined IP and port values to start the server when the script is executed.

## Additional concept
- In this project we use Tkinter to provide graphical user-friendly interface (GUI) for the user, making it easier for them to  interact to search news headlines, view sources, and explore detailed articles. Moreover, we use OOP (CustomDialog class) to organize the code and simplify the management of user input functionality. and we inherit 'simpledialog.Dialog ' from the class to customizing behavior to fit the application's needs.

## Acknowledgments 
I would like to express to eveyone who contributed to the development of this application:
- Mentor for his invaluable guidance and support throughout the project.
- NewsAPI.org for offering a robust API that enabled real-time news integration, significantly enhancing the application's functionality.
- Al-Munthir Saffan youtube channel for good explaination about creating GUI .


## conclution
This project successfully demonstrates the integration of a client-server architecture with a user-friendly GUI and real-time data fetching from NewsAPI.org. 


