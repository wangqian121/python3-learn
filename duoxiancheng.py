import threading
import time
def run(name):
    print(name,"线程执行了")
    time.sleep(6)
#创建线程
t1=threading.Thread(target=run,args=("t1",))
t3=threading.Thread(target=run,args=("t3",))
t2=threading.Thread(target=run,args=("t2",))
#启动线程
t3.start()
t1.start()
t2.start()
#程序执行时，程序本身是一个线程叫主线程，手动创建的线程叫子线程，主线程的执行中不会等待子线程执行完，就会执行后面的代码
# t1.join()#设置等待子线程执行完毕，主线程才会执行
# t2.join()
# t3.join()
print("执行完毕")

