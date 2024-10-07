'''
This script demonstrates how to use time.sleep function
'''

import threading
import time

class myThread(threading.Thread):
    __terminate=False  # 这是一个私有变量，用于指示线程是否应该终止。默认值为 False。
    __count=0  # 这是另一个私有变量，用于记录线程运行的计数。
    
    # 当调用该方法时，将 __terminate 设置为 True，从而指示 count() 方法停止执行。
    def terminate(self):
        self.__terminate=True
    
    # 定义计数和显示功能
    # count(): 在一个 while 循环中不断增加 __count 的值，直到 __terminate 被设置为 True。每次循环暂停1秒。
    def count(self):
        while not self.__terminate:
            self.__count+=1
            time.sleep(1)
        print("Thread terminated, count to "+str(self.__count))
    # display() ：打印当前的计数值 __count。
    def display(self):
        print(self.__count)
    
    # run() 方法会在调用 start() 时执行，实际上会调用 count() 方法。
    def run(self):
        self.count()

# 启动线程并显示计数
t1=myThread()  # Step1: 创建 myThread 的实例。
t1.start()     # Step2: 启动线程，调用 run() 方法, 实际上调用count()方法，此时子线程进入count()方法的while循环，开始增加__count的值
# Step3: 主线程循环，主线程在循环中每两秒调用一次 display()，打印当前的计数。
for i in range(5):  # range(5) 0 1 2 3 4
    t1.display()
    time.sleep(2)
t1.terminate() # 在主线程的循环结束后，调用 terminate() 方法以终止子线程。
