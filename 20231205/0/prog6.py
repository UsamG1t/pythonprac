import asyncio

class Q(asyncio.Queue):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        return super().__init__(*args, **kwargs)
    def __str__(self):
        return f'<{self.name}>'

async def prod(queue1):
    for i in range(5):
        await queue1.put(f'value_{i}')
        print(f'prod: put {i} to {queue1}')
        await asyncio.sleep(1)
    await queue1.put(None)


async def mid(queue1, queue2):
    while True:
        value = await queue1.get()
        
        if value == None:
            await queue2.put(value)
            return

        print(f'mid: got {int(value[-1])} from {queue1}')
        await queue2.put(value)
        print(f'mid: put {int(value[-1])} to {queue2}')

async def cons(queue2):
    while True:
        value = await queue2.get()
        
        if value == None:
            return
        
        print(f'cons: got {int(value[-1])} from {queue2}')

async def main():
    queue1, queue2 = Q('John'), Q('Jack')
    await asyncio.gather(
        prod(queue1),
        mid(queue1, queue2),
        cons(queue2))

asyncio.run(main())    