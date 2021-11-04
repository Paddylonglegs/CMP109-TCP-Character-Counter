# CMP109-TCP-Character-Counter
Simple character/word counter using python socket programming, TCP server and client

Client: import socket is used, a text file has been created outside of python/visual studio code. This text file "contents.txt" is opened and read. The message is displayed client side just to show user the message. The read contents of the text file is turned into a string to be sent across to the server. This is then encoded and sent to the server. The returned message from the server is split up into 2, one for characters and one for words. They are then displayed to the console and the user knows how many characters and words are in the text file.

Server: Displayed message lets the user know the server is ready. The characters of the text file is done by using len(INCOMING_MESSAGE) as this will count the length of the message. The same len is used to find how many words are in the INCOMING_MESSAGE, however the message is split when it's receieved so it will just count the spaces between the splits and display that as the number of words.

Finally, the character variable and word variable is combined like seen in the UDP calculator client. The combined message is turned into a string and encoded which is sent back to the client and then decodes and splits up this message.
