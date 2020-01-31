import socket
server =socket.socket()#生成socket连接对象
server.bind(("localhost",6969))#绑定监听对象
server.listen()#监听
print("准备接电话了")
con,addr=server.accept()#等待消息
print("con的值是：",con,"addr的值是：",addr)
date=con.recv(1024)#接收消息
print("接收到的消息",date)
server.close()