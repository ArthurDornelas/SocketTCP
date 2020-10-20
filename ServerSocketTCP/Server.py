from socket import *
from pip._vendor.distlib.compat import raw_input

serverPort = 3030
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print('Esse servidor esta pronto para receber')
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode()
    print('Do Cliente: ', sentence)
    serverMessage = raw_input('Escreva a resposta:')
    connectionSocket.send(serverMessage.encode())
    connectionSocket.close()
