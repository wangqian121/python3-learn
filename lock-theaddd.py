import threading
#创建线程锁也叫互斥锁
lock=threading.Lock()
num=100
def run(name):
    lock.acquire()#设置锁
    global num #设置num为全局变量
    num=num-1
    print("线程",num,"执行了，目前num的值为：",num)
    lock.release()#释放锁
    #创建并启动100个线程
for i in range(100):
        t=threading.Thread(target=run,args=("i+1",))
        t.start()
#全局解释器锁（GIL）
#无论cpu核心数量多少，都保证程python序只能执行一个线程，造成cpu浪费和执行效率减慢
#使用多进程解决GIL带来的问题