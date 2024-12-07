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
- connect to server and send the user input to the server .
- receives and displays the server's response.

+ Utilized packeges:
- socket for network communication.
- tkinter to creat GUI .

+ Functions and Classes: 
- NewsClient class 
- connect_to_server function to start connection with server.
- create_widgets function to set up main menu interface.
- search_headline function to open seperate window for " search headlines", and create button for parameters of search using headline. 
- for each category parameter in search by headline we create function (search_by_keyword / search_by_category / search_by_country / list_all_headlines ) to take input from user -> send it to the server, then show the result in screen for user 
- list_sources function to open seperate window for "list sources ", and create button for parameters of list sources.
- for each category in list by sources we create function (source_by_category / source_by_country / source_by_language / list_all_sources ) to take input from user -> send it to the server, then show the result in screen for user.
- show_results function to show details about specefic topic.
- show_message function to display the response.
- quit function for guit the program.

2. Server scripts
 Main functionality:
- listens for incoming client connections.
- processes client requests.
- Sends responses back to the clients.

 Utilized packeges:
- socket for network communication.
- threading for handling multiple clients concurrently.
- json for encoding and decoding JSON data.

Functions and Classes: 
- handle_client function to handles communication with a connected client. 
- start_server to start the server and listen for incoming connections.

## Additional concept
- In this project we use Tkinter to provide graphical user-friendly interface (GUI) for the user, by providing visual elements like buttons, labels, and entry fields, making it easier for users to interact with the application. 

## Acknowledgments 
I would like to express to eveyone who contributed to the development of this application:
- Mentor for his invaluable guidance and support throughout the project.
- NewsAPI.org for offering a robust API that enabled real-time news integration, significantly enhancing the application's functionality.
- Al-Munthir Saffan youtube channel for good explaination about how GUI work.


## conclution
This project successfully demonstrates the integration of a client-server architecture with a user-friendly GUI and real-time data fetching from NewsAPI.org. T


