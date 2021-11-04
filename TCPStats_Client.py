'''
Name: TCP_client.py
Desc: an example TCP client
Auth: Patrick Collins
Date: 29/11/19
©️license MIT
https://github.com/Paddylonglegs/
'''
import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 54321

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLIENT_SOCKET.connect((SERVER_HOST, SERVER_PORT)) #3-way TCP handshake.

SENT_MESSAGE = open("contents.txt", "r") #Opening the text file that will be read.

if SENT_MESSAGE.mode == "r": #Making sure the file mode is read.
    Contents = SENT_MESSAGE.read() #Declaring variable to read the message in the text file.
    print('Contents of text file is: ', Contents) #Displaying contents of the text file, simply for the user's pleasure.


CONTENTS = str(Contents) #Turning into bytes like value/ string.

CLIENT_SOCKET.sendall(CONTENTS.encode()) #Encoding the contents to send over the TCP Server.

RECEIVED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(4096) #Sending the contents to the TCP Server.

RECEIVED_MESSAGE = RECEIVED_MESSAGE.decode().split(',') #Splitting message into two. One for the number of characters and one for number of words.
print('Number of characters: ', RECEIVED_MESSAGE[0]) #Assigning split value to print, the first in the split is the number of Characters.
print('Number of Words: ', RECEIVED_MESSAGE[1])  #Assigning split value to print, the second in the split is the number of Words.

CLIENT_SOCKET.close()