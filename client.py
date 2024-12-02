import socket

username=input("Enter your username")

host="127.0.0.1"
port= 13256
#create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(host , port)
    s.send("User name:", username)
    
    data= s.recv(1024)
    print(f"received {data}")