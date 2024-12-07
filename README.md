# Multithreading-News-Information-System
## Project Description
This project is a multithreaded news information system that allows users to search for news from https://newsapi.org articles based headlines or sources and by specifying (keyword, country, category, ..). The system connect users to threads and handle various users at time.
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
pip install newsapi-python \
Ensure that you have Python installed on your system. \
Ensure that you have the required libraries and modules:
- json
- socket
- threading
- os
## How to Run
1. Run the server.py file on the server machine.
2. Run the client.py file on the client machine.
3. Follow the instructions on the client interface to search for news articles.
## client-server scripts 
1. Client scripts
+ Main functionalities: 
- connect to server.

- send the user name to the server .

- receives and displays the server's response until it quit.

+ Utilized packeges:
- socket for network communication.

- tkinter to creat GUI .

- from tkinter import messagebox, simpledialog to display pop-up message boxes, and prompt the user for simple input via dialog boxes in the Tkinter GUI.

+ Functions and Classes: 
- connect_to_server function start connection with server.

- create_widgets function create main menu interface.

- update_frame function clears the main frame and update it with new content.

- search_headlines function updates the main frame to show options for searching headlines.

- search_headlines_content function provides the UI elements for searching headlines

- for each category parameter in search by headline we create function (search_by_keyword / search_by_category / search_by_country / list_all_headlines ) to take input from user, then send it to server for processing .

- list_sources function updates the main frame to show options for listing news sources.

- list_sources_content function provides the UI for searching news sources.

- for each category in list by sources we create function (source_by_category / source_by_country / source_by_language / list_all_sources ) to take input from user, then send it to the server to process it.

- show_results function displays the results of the search (either headlines or sources) in a text area, and  allows the user to select an article number to view more details about a specific article.

- show_message function displays a message in a pop-up message box.

- quit function  handles the application quitting process.

2. Server scripts
 Main functionality:

- listens for incoming client connections.

- accept clients and put them in threat , then send greeting with client name

- processes client requests.

- click for the result if it save on file or not, if not request for the results and save them in json file.

- Sends responses back to the clients.

 Utilized packeges

 - from newsapi import NewsApiClient for import NewsApiClient class from the newsapi library.

- socket for network communication.

- threading for handling multiple clients concurrently.

- json for create json file.

- os to make sure if file available or need request.

Functions and Classes: 
- handle_client function to handles communication with a connected client. 

- start_server to start the server and listen for incoming connections.

## Additional concept
- In this project we use Tkinter to provide graphical user-friendly interface (GUI) for the user, making it easier for them to  interact to search news headlines, view sources, and explore detailed articles. 

## Acknowledgments 
I would like to express to eveyone who contributed to the development of this application:
- Mentor for his invaluable guidance and support throughout the project.
- NewsAPI.org for offering a robust API that enabled real-time news integration, significantly enhancing the application's functionality.
- Al-Munthir Saffan youtube channel for good explaination about creating GUI .


## conclution
This project successfully demonstrates the integration of a client-server architecture with a user-friendly GUI and real-time data fetching from NewsAPI.org. 


