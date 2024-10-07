'''
这个代码演示了如何通过继承 threading.Thread 类创建并运行多个线程

要控制主线程等待所有子线程完成后再打印完成信息，你可以使用 thread.join() 方法。该方法会阻塞主线程，直到调用 join() 的子线程执行完毕。
i.join()

'''

import threading
import time

#create a class
class myThread(threading.Thread):
    # __init__在类初始化时被调用。通过调用父类的 __init__() 方法，确保线程类正常初始化，并且接收一个 threadID 参数，用于标识每个线程。
    def __init__(self, threadID):  
        threading.Thread.__init__(self)
        self.threadID=threadID   # self.threadID: 这是线程的唯一标识符，它被保存在每个线程对象中
    # 覆盖 run 方法: 当调用 start() 方法时，线程将会自动执行 run() 方法中的代码
    def run(self):
        print("This is thread - "+str(self.threadID))  # 线程首先打印一个标识信息
        time.sleep(1)     # 通过 time.sleep(1) 暂停1秒，模拟任务执行的延迟                     
        print("Thread"+str(self.threadID)+"terminates!")  # 打印线程终止的消息

# Create five threads 创建并启动多个线程
threads=[]
for i in range(5):  # 用于创建5个线程，每个线程被分配一个不同的 threadID。
    threadTemp=myThread(i)
    threadTemp.start()   # 启动线程，开始执行 run() 方法。此时，线程将会在后台并行执行。
    threads.append(threadTemp)   # threads.append(threadTemp): 将每个线程对象保存到列表 threads 中，方便后续操作。

# Wait for all threads to be completed.  等待所有线程完成
for i in threads:
    i.join() # 阻塞主线程，直到 i 线程完成。join() 方法确保主线程等待所有创建的线程执行完毕后才继续往下执行。这里是为了保证所有线程执行完毕后，再输出主线程的退出消息。

print("Exit main thread!")