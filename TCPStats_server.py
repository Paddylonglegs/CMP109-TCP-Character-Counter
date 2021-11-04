'''
Name: TCP_server.py
Desc: an example TCP server
Auth: Patrick Collins
Date: 29/11/19
©️license MIT
https://github.com/Paddylonglegs/
'''

import socket
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 54321

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_SOCKET.bind((SERVER_HOST, SERVER_PORT))
print('Server is ready') #Letting the user know the server is ready to go

SERVER_SOCKET.listen()

INCOMING_CONNECTION, CLIENT_ADDRESS = SERVER_SOCKET.accept()


while True:
    INCOMING_MESSAGE = INCOMING_CONNECTION.recv(4096)
    wordSplit = INCOMING_MESSAGE.split() #Splitting the message, this is to count how many spaces there are in the text file which is how mnany words there are.
    if not INCOMING_MESSAGE:
        break
    number_of_characters = len(INCOMING_MESSAGE) #Get the number of characters by length of the data in the text file.
    print('Number of characters in text file :', number_of_characters) #Displaying number of characters at server side.

    number_of_words = len(wordSplit) #Get the number of words in the text file.
    print('Number of words: ', number_of_words) #Displaying number of words at server side.

    CHARS = str(number_of_characters) #Turning the int value of the number of characters to a string. Bytes like value.
    WORDS = str(number_of_words) #Turning the int value of the number of words to a string. Bytes like value.
    BOTH = CHARS + ',' + WORDS + ',' #Turning the Character and Words into a string that is able to be split up using ','.
    ALL = str(BOTH) #Turning the Both value to a string, so it's able to be sent back to the client.
    
    INCOMING_CONNECTION.sendall(ALL.encode()) #Sending the encoded results back to the client.
    


SERVER_SOCKET.close()