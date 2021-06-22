import asyncio
from threading import Thread
from multiprocessing import Process
from time import sleep
from LibF.GPA import *

#Mutli Thread Concurrency

#"@MAN.main.task" adds the function below to a tasks list
@MAN.main.task
#MAN is a built in manager for having up to 4 concurrent threads
async def helloWorld():
    for i in range(3):
        print("Hello World!")
        await asyncio.sleep(0.2)

@MAN.main.task
async def anotherOne():
    for i in range(3):
        print("I'm running concurrently!")
        await asyncio.sleep(0.1)

@MAN.side.task
#MAN is a built in manager for having up to 4 concurrent threads (class 'MTManager')
async def pythonista():
    for i in range(3):
        print("We love Python!")
        await asyncio.sleep(0.1)

@MAN.side.task
async def anotherThread():
    for i in range(3):
        print("I'm on another thread!")
        await asyncio.sleep(0.1)

#Execution looks like this when using multiple threads
if __name__ == '__main__':
    #Man has 4 available threads: main, side, back, and util
    T1 = Thread(target=MAN.main.run, args=())
    T2 = Thread(target=MAN.side.run, args=())
    #You could also run other functions in one of the threads, for example:
    T3 = Thread(target=print,args=("Third Thread"))
    T1.start()
    T2.start()
    T3.start()
    #T1.join() <- You may join the threads if you so choose