import asyncio
from threading import Thread
from time import sleep
from LibF.GPA import *

Main = Queue()

#Single Thread Concurrency

#"@Main.task" adds the function below to a tasks list
@Main.task
async def helloWorld():
    for i in range(3):
        print("Hello World!")
        await asyncio.sleep(0.1)

@Main.task
async def anotherOne():
    for i in range(3):
        print("I'm running concurrently!")
        await asyncio.sleep(0.1)

#Begin execution
Main.run()