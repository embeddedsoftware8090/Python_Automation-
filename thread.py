#-Currenct Execution thread

# import threading
# print("Current Executing Thread: ",threading.currentThread().getName())

#create a threadwithout using any class------------------

# from threading import *
# def display():
#     for i in range(1,11):
#         print("Child Thread")
# t=Thread(target=display())#creating thread object
# t.start() #starting the thread
# for i in range(1,11):
#     print("Main Thread")

#craeting a thread by extending thread class----
# from threading import *
# class MyThread(Thread):
#     def run(self) :
#         for i in range(10):
#             print("Child Thread-1")
# t=MyThread()
# t.start()
# for i in range(10):
#     print("Main Thread-1")
#

#--
# import threading
# for thread in threading.enumerate():
#     print(thread.name)
#
# import threading
#
# def worker(argument):
#     print(argument)
#     return
#
# for i in range(5):
#     t = threading.Thread(target=worker, args=[i])
#     t.start()

import threading
for thread in threading.enumerate():
    print(thread.run())