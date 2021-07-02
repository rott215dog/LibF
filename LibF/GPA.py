import asyncio
from typing import Dict, List, Any, Optional, Callable, Awaitable
from threading import Thread
from time import sleep

class Frame:
    def __init__(
        self,
        loop: Optional[asyncio.AbstractEventLoop] = None
    ) -> None:

        #self.loop = loop or asyncio.get_event_loop()

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        self.tasks: List[Callable[[], Awaitable[None]]] = []

        self.argtasks: Dict[ str, Any ] = {}

        self.argus: Dict[ str, List() ] = {}

        self._running_tasks: List[asyncio.Future[Any]] = []

    def task(self, func: Callable[[], Awaitable[None]]) -> None:
        self.tasks.append(func)

    def event(self, args) -> Callable[[Callable[[], Awaitable[None]]], Callable[[], Awaitable[None]]]:
        def wrapper(func: Callable[[], Awaitable[None]]) -> Callable[[], Awaitable[None]]:
            #func.__name__
            self.argtasks[func.__name__] = func
            self.argus[func.__name__] = args
            return func
        return wrapper

    async def start_tasks(self) -> None:
        runem = []
        for r in self.tasks:
            runem.append(r())
        await asyncio.gather(*runem)

    async def arg_start(self) -> None:
        runim = []
        for i in self.argtasks:
            if self.argus[i] != []:
                for p in self.argus[i]:
                    runim.append(self.argtasks[i](p))
            else:
                runim.append(self.argtasks[i]())
        await asyncio.gather(*runim)

    def stop_tasks(self) -> None:
        for t in self._running_tasks:
            if not t.cancelled():
                t.cancel()

class Queue(Frame):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def run(self) -> None:
        try:
            self.loop.run_until_complete(self.start())
        except KeyboardInterrupt:
            pass

    def argrun(self) -> None:
        try:
            self.loop.run_until_complete(self.argstart())
        except KeyboardInterrupt:
            pass
    
    async def stop(self) -> None:
        self.stop_tasks()
        exit(-1)

    async def start(self) -> None:
        await self.start_tasks()
        #await self.main_loop()
    
    async def argstart(self) -> None:
        await self.arg_start()

    async def main_loop(self) -> None:
        while True:
            await asyncio.sleep(0)


class MTManager:
    def __init__(self):
        self.main = Queue()
        self.side = Queue()
        self.back = Queue()
        self.util = Queue()

MAN = MTManager()

class SyncQueue:

  #[(function, [cases])]
  def __init__(self):
    self.tasks = []

  def run(self,pause=None):
    if pause == None:
      for exe in self.tasks:
        if len(exe[1]) != 0:
            for case in exe[1]:
                exe[0](case)
        else:
            exe[0]()
      self.tasks = []
    else:
      for exe in range(pause):
        fun = self.tasks[exe]
        if len(fun[1]) != 0:
            for case in fun[1]:
                fun[0](case)
        else:
            exe[0]()
        self.tasks.pop(exe)

  def add(self,f,c):
    self.tasks.append((f,c))

  def __repr__(self):
    return str(self.tasks)

def Kill(q):
    asyncio.run(q.stop())

#My reference
Main = Queue()

@Main.event([4,5,6])
async def timer(a):
    print(a)
    if a == 4 or a == 5:
        await asyncio.sleep(0.1)
    else:
        await asyncio.sleep(2)
    print(str(a) + 'NEXT')
    await asyncio.sleep(0.1)

@Main.event([])
async def printer(a=9):
    for i in range(3):
        print(a)
        await asyncio.sleep(0.1)

@Main.event([])
async def helloWorld():
    for i in range(3):
        print("Hello World!")
        await asyncio.sleep(0.1)

@Main.event([])
async def anotherOne():
    for i in range(3):
        print("I'm running concurrently!")
        await asyncio.sleep(0.1)

Main.argrun()

@Main.task
async def helloWorld2():
    for i in range(3):
        print("Hello World! 2")
        await asyncio.sleep(0.1)

@Main.task
async def anotherOne2():
    for i in range(3):
        print("I'm running concurrently! 2")
        await asyncio.sleep(0.1)

Main.run()

Kill(Main)