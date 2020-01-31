#文件读写
wj=open(r"/Users/wangqian/Downloads/测试地址.txt","r",encoding='GBK')
data=wj.read()
print(data)
wj.close()
#读取文件
fh=open("/Users/wangqian/Downloads/测试地址.txt","r",encoding='GBK')
date1=fh.readline()
date2=fh.readline()
date3=fh.readline()
date1=fh.readlines()
print(date1[1])
# # print(date1)
# # print(date2)
# # print(date3)
# fh.close()
for i in fh:
    print(i)
fh.close()
#文件写入,w会将之前的内容覆盖，显示新写入的，如果没有001这个文件，会自动创建该文件
fh=open("/Users/wangqian/Downloads/001.txt","w",encoding='GBK')
fh.write("hhhhh")
fh.close()
fh=open("/Users/wangqian/Downloads/001.txt","a")#a代表append，追加
date=("\n文件写入，你明白了吗")
fh.write(date)
fh.close()
#二进制文件的读写
fh=open("/Users/wangqian/Desktop/aa.png",'rb')
date1=fh.read()
fh.close()
fh1=open("/Users/wangqian/Downloads/aa.png",'wb')
fh1.write(date1)
fh1.close()
