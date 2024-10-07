'''
This script domonstrates how to use a timer in a sperate thread to control the loop 如何在单独的线程中使用计时器来控制循环
'''

import threading
import time

class myThread():
    __terminate=False  # 是一个类属性，默认为 False，用于控制计数的终止。
    # 这个构造函数接收一个参数 timer，表示计时器的持续时间。
    def __init__(self, timer):
        self.__timer=timer
    # 计数方法：这个方法实现一个循环，直到 __terminate 被设置为 True。每次循环，计数器 i 增加1，并且每秒暂停一次。
    def count(self):
        i=0
        while not self.__terminate:
            i+=1
            time.sleep(1)
        print("Thread terminated, count to "+str(i))

    # 计时器方法: 这个方法使当前线程暂停指定的 __timer 秒后，将 __terminate 设置为 True，以终止计数。
    def timer(self):
        time.sleep(self.__timer)
        self.__terminate=True

    # 运行方法: 启动两个线程：一个用于计数，另一个用于计时
    def run(self):
        t1=threading.Thread(target=self.count)
        t2=threading.Thread(target=self.timer)
        t1.start()
        t2.start()

# 创建两个 myThread 对象，分别设置计时器为 30 秒和 5 秒，并调用 run() 方法启动线程。
thread1=myThread(30)  # thread1 的计时器将持续 30 秒
thread1.run()
thread2=myThread(5)   # thread2 的计时器将持续 5 秒
thread2.run()
