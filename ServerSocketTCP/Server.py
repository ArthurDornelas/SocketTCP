from socket import *
from pip._vendor.distlib.compat import raw_input

serverPort = 3030
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print('Esse servidor esta pronto para receber')
while 1:
    try:
        connectionSocket, addr = serverSocket.accept()
        while 1:
            sentence = connectionSocket.recv(4096).decode()
            if sentence == '/q':
                serverMessage = 'Conexao finalizada'
                connectionSocket.send(serverMessage.encode())
                break
            else:
                print('Do Cliente: ', sentence)
                serverMessage = raw_input('Escreva a resposta:')
                connectionSocket.send(serverMessage.encode())
        print('Finalizando conexao com cliente...')
        connectionSocket.close()
    except OSError:
        break
