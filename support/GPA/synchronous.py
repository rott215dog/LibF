import asyncio
from threading import Thread
from time import sleep
from LibF.GPA import *

#LibF - GPA provides a simple and easy way to create Synchronous Queues
#Unlike Async Queues, Sync Queues will run each function until completion before beginning the next

#Initialize a Queue
sync = SyncQueue()

sync.add(print,['Hello World!']) #.add takes two arguments, a function and args for that function
sync.add(print,["I love Python!"])

def hi():
    print("HI")

sync.add(hi,[])

sync.run()

#You can also move the SyncQueue a limited number of times by using:
#sync.run(1) <- Can be any integer that does not exceed the amount of tasks
#^^^ This will only execute one task and then remove it from the list

#TIP: sync.run() works in multithreading, so one thread can one line-by-line while another runs asynchronously