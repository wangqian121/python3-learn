import threading
#创建线程锁
lock=threading.Lock()
num=100
#卖票
def sale(name):
    lock.acquire()
    global num
    if num>0:
        num=num-1
        print(name,"卖出一张票，还剩票数：",num)
    lock.release()
    #卖票窗口
while 1==1:
    if num>0:
        t1=threading.Thread(target=sale,args=("1号窗口",))
        t2 = threading.Thread(target=sale, args=("2号窗口",))
        t1.start()
        t2.start()
    else:
        break
print("票卖完了")





