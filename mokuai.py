#导入随机数模块
# import random
# # a=random.random()#随机生成0-1之间的数
# # b=random.choice(["张三","李四","王五"])
# # print(b)
#爬取百度首页
# from urllib import request
# url="http://www.baidu.com"
# date=request.urlopen(url).read()
# print(date.decode())
# import os
# # os.system("/Applications/Photos.app")
# os.rename(r"/Users/wangqian/Desktop/王倩.pdf",r"/Users/wangqian/Desktop/wangqian.pdf")
# import webbrowser
# webbrowser.open("http://www.baidu.com")
from PIL import Image,ImageFilter
im=Image.open("/Users/wangqian/Desktop/aa.png")#打开照片
im2=im.filter(ImageFilter.BLUR)#启用模糊滤镜
im2.save("/Users/wangqian/Desktop/bb.png")#保存图片