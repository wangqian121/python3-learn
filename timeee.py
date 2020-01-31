import datetime
#获取当前时间
# now=datetime.datetime.now()
# print(now)
# #获取指定日期
# s=datetime.datetime(2019,8,21,10,21,3)
# print(s)
#日期转字符串
# now=datetime.datetime.now()
# d=now.strftime("%Y-%m-%d %H:%M:%S")
# print(type(d))
#字符串转日期
s="2020-9-18 8:29:29"
ss=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
print(type(ss))
