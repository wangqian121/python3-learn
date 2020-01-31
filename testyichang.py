# a=(1,2,3,4,34,45,"a",57,0)
# for i in a:
#     print("i的值是：",i)
#     try:#写可能会出现报错或出现异常的代码
#         print(4/i)
#     except Exception as e:#捕获try语句里面的异常，Exception就是捕获到的异常对象
#         print("出现的错误是：",e)#出现异常时执行的语句
#     else:
#         print("....正常")#没有异常时执行的语句
#     finally:
#         print("执行结束")#不管是否有异常都会执行的语句



pwd="123456"
if len(pwd)<=8:
    ex=Exception("密码不能小于8位")
    raise ex  #抛出自定义异常
else:
    print("密码设置成功")