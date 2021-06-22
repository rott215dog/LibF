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

        self._running_tasks: List[asyncio.Future[Any]] = []

    def task(self, func: Callable[[], Awaitable[None]]) -> None:
        self.tasks.append(func)

    async def start_tasks(self) -> None:
        for func in self.tasks:
            t = self.loop.create_task(func())
            self._running_tasks.append(t)

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
        finally:
            self.loop.run_until_complete(self.stop())

    async def stop(self) -> None:
        self.stop_tasks()
        exit(-1)

    async def start(self) -> None:
        await self.start_tasks()
        await self.main_loop()

    async def main_loop(self) -> None:
        while True:
            if self._running_tasks == []:
                break
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