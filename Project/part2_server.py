# Group#: G18
# Student Names: Josiann Zhou, Kevin Peng

from socket import *
import time
import random

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) # create UDP socket
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048) # read message from client
    modifiedMessage = message.decode().split("-")[0] + "- ditto" # copy PING and replace message with ditto
    rand_fail = random.randrange(1,10) # create a random 10% fail rate
    if rand_fail != 1:
        time.sleep(random.randrange(5, 50)/1000) # divide by 1000 to get ms instead of seconds
        serverSocket.sendto(modifiedMessage.encode(), clientAddress) # send echo to client