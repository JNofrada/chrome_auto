import chrome_bookmarks
import webbrowser
import sys
import time
import pytest
import socket

HOST = '127.0.0.42'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print( f'Connection from {address} has been established')
    clientsocket.send(bytes("Welcome to the server", "utf-8"))



#def main():
#    for url in chrome_bookmarks.urls:
 #       print(url.name)
  #      time.sleep(1)
   #    if (url.url == 'https://valiantny.sharepoint.com/sites/CMChangeManagement' or url.url == 'https://developers.google.com/api-client-library/python/'):
    #        continue
     #   webbrowser.open(url.url)
    #sys.exit("0")

#if __name__ == '__main()__':
 #   main()
 
