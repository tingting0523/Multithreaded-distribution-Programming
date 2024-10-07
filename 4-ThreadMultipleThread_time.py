'''
This example illustrate how to use time.sleep() function
'''

import threading
import time

#create a class

class myThread(threading.Thread):
    # 构造函数初始化了线程，并且 threadID 被用作线程的标识符，它也用于控制 time.sleep() 的暂停时间。
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID=threadID
    # 当线程启动时，会执行 run() 方法
    def run(self):
        print("This is thread - "+str(self.threadID))   # 首先输出线程的 threadID。
        #The time.sleep(t) function takes one argument "t", indicates the number of seconds 
        #an execution to be suspended
        time.sleep(self.threadID)  # 通过 time.sleep(self.threadID) 暂停执行，self.threadID 的值决定了线程会暂停几秒。
        print("Thread"+str(self.threadID)+" terminates!")  # 输出线程结束的消息
        
#create 5 threads, the number of seconds that each thread to be suspended are 1, 2, 3, 4, 5  创建了5个线程，每个线程的 threadID 值从1到5，这决定了每个线程的暂停时间：第一个线程暂停1秒，第二个线程暂停2秒...
for i in range(1,6):
    threadTemp=myThread(i)
    threadTemp.start() # 启动线程，这会调用线程的 run() 方法。
    
print("Exit main thread!")