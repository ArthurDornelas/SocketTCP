from socket import *
from pip._vendor.distlib.compat import raw_input

serverName = 'localhost'
serverPort = 3030
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while 1:
    try:
        message = raw_input('Escreva a mensagem (Digite "/q"  para finalizar a conexao):')
        clientSocket.send(message.encode())
        responseMessage = clientSocket.recv(4096).decode()
        print('Do servidor:', responseMessage)
        if(responseMessage == 'Conexao finalizada'):
            clientSocket.close()
            exit()
    except OSError:
        break


