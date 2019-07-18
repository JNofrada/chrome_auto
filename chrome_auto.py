import webbrowser
import socket

HOST = '127.0.0.42'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

msg = s.recv(1024)
print(msg.decode("utf-8"))

pause = input("Press Enter to leave")