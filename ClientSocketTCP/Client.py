from socket import *
from pip._vendor.distlib.compat import raw_input

serverName = 'localhost'
serverPort = 3030
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while 1:
    message = raw_input('Escreva a mensagem:')
    clientSocket.send(message.encode())
    responseMessage = clientSocket.recv(2048)
    print('Do servidor:', responseMessage.decode())
    clientSocket.close()
