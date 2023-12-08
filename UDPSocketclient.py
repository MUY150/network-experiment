from socket import*
import os
def main():
    serverName =input('Input ServerAddress:')
    serverPort =int(input('Input ServerPort:'))
    clientSocket=socket(AF_INET,SOCK_DGRAM)
    _PATH=input('Input File_Path:')
    a=open(_PATH,'rb')
    eof=a.seek(0,2)
    (_path,filename)=os.path.split(_PATH)
    clientSocket.sendto(filename.encode(),(serverName,serverPort))#把文件名传过去
    firstflag,serverAddress=clientSocket.recvfrom(2048)
    print('From Server: ', firstflag.decode())
    if firstflag.decode()=='ok':   
        a.seek(0,0)       
        while True:
            line=a.read(512)
            if line==None:
                print(_PATH," is empty!")#内容为空
                clientSocket.sendto('end'.encode(),(serverName,serverPort))
                exit(0)
            clientSocket.sendto(line,(serverName,serverPort))
            flag,(serverip,serverport)=clientSocket.recvfrom(2048)   
            while flag.decode()!="ok":
                clientSocket.sendto(line,(serverName,serverPort))
                flag,(serverip,serverport)=clientSocket.recvfrom(2048)  #重传                          
            if a.tell()>=eof :break   #读到文件尾或超过文件尾退出循环                  
    a.close()       
    clientSocket.sendto('end'.encode(),(serverName,serverPort))#表明传输完成
    clientSocket.close

main()