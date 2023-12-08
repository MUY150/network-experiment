from socket import*
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The Server is ready to receive")
while True:
    filename,clientAddress=serverSocket.recvfrom(2048)
    _PATH="./"+filename.decode()
    a=open(_PATH,'wb')
    serverSocket.sendto('ok'.encode(),clientAddress)#表明已经准备好了
    while True:
        message,clientAddress=serverSocket.recvfrom(2048)
        if message=='end'.encode(): break
        a.write(message)#写入
        serverSocket.sendto("ok".encode(),clientAddress)#表明已经准备好了接收下一串数据
    a.close()
    print('finished')
            