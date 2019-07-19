import webbrowser
import socket

HOST = '172.20.1.232'
PORT = 5000
CONNECTED = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Attempting to connect")
s.connect((HOST, PORT))
s.send(bytes("Hello Server", "utf-8"))

msg = s.recv(1024)
print(msg.decode("utf-8"))

pause = input("Press Enter to leave")
