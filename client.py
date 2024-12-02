import socket

#host and port
Host='127.0.0.1'
Port= 12354

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host,Port))
    s.listen
    connection , address = s.accept()