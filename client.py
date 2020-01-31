import socket
client=socket.socket()#生成socket连接对象
client.connect(("localhost",6969))#和目标主机连接
client.send("hello world".encode())#发送内容
client.close()