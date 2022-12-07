# Group#: G18
# Student Names: Josiann Zhou, Kevin Peng

from socket import *
import time

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET,  SOCK_DGRAM) # create UDP socket
clientSocket.settimeout(1) # set timeout for receiving messge from server to 1s
num = 1

while num < 6: # send ping 5 times
    message = f"PING {num} - hello world"
    send_time = time.time()
    clientSocket.sendto(message.encode(), (serverName, serverPort)) # send message to server
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # receive echo
        acknowledge_time = time.time()
        # calculate RTT as: Time echoed response was received - Time message was sent
        rtt = acknowledge_time - send_time
        modifiedMessage = modifiedMessage.decode()
        print (modifiedMessage, rtt)
    except timeout:
        print("request timed out")
    num += 1

clientSocket.close()