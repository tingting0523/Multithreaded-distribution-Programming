# Three methods to create a thread.
import threading


############### 创建线程并调用无参数函数 ############### 
#Thread example: function without args  定义了一个不带参数的函数，作为线程要执行的任务。
def threadFunction1():
    print("This is thread 1\n ")

#Create a thread 创建了一个线程
thread1=threading.Thread(target=threadFunction1)   # target 参数指定要执行的函数（threadFunction1）。线程被创建时并没有立即执行任务。

thread1.start() #Start the thread 启动线程，线程开始执行 threadFunction1 函数。



############### 创建线程并调用带参数的函数 ###############
#Thread example: function with args 定义了一个带参数的函数，参数 name 会在执行时传入。
def threadFunction2(name):
    print("This is thread "+name)
    
#create a thread 创建了一个线程
thread2=threading.Thread(target=threadFunction2, args=["thread2"]) # target 指定要执行的函数，args 用于传递参数给该函数。这里 args 是一个元组，所以即使只有一个参数，也必须用方括号包裹。

thread2.start() # 启动线程，线程开始执行 threadFunction2("thread2")。


############### 通过类创建线程 ###############
#Create thread in class 创建了一个自定义线程类，继承自 threading.Thread。
class myThread(threading.Thread):
    #override run function  在类内部，覆盖了 run() 方法，这个方法定义了线程启动时执行的操作。
    def run(self):
        print("Thread - 3")
        
#Create a new thread:
thread3=myThread()  # 创建一个 myThread 类的实例，即一个新线程对象。
thread3.start() # 启动线程，会自动调用类中的 run() 方法，执行其中的代码。输出 Thread - 3。
