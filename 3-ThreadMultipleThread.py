import threading

#create a class

class myThread(threading.Thread):
    # __init__: 构造函数中调用了 threading.Thread.__init__(self)，这确保了线程类正确初始化。threadID 被用来给每个线程一个唯一的标识符。
    def __init__(self, threadID): 
        threading.Thread.__init__(self)
        self.threadID=threadID
    # run(): 当线程启动时会自动执行 run() 方法。这里每个线程的 run 方法都打印出线程的 threadID。
    def run(self):
        print("This is thread - "+str(self.threadID))
        

for i in range(5): # 创建5个线程，每个线程的 threadID 值从0到4。
    threadTemp=myThread(i)
    threadTemp.start() # 启动线程并自动调用 run() 方法。每个线程会并行执行，输出它的 threadID。
