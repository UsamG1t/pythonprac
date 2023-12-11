import asyncio
class G:
    event = None

async def writer(queue, delay):
    number = 0
    while True:
        await asyncio.sleep(delay)
        if G.event:
            return None
        await queue.put(f'{number}_{delay}')
        number += 1

async def stacker(queue, stack):
    while True:
        await asyncio.sleep(0)
        # if queue._queue:
        try:
            stack.append(queue.get_nowait())
        except asyncio.QueueEmpty:
            pass
        if G.event:
            return None

async def reader(stack, count, delay):
    while count:
        await asyncio.sleep(delay)
        while not stack:
            await asyncio.sleep(0)
        value = stack.pop()
        print(value)
        count -= 1
    G.event = 1
    return None

async def main():
    queue = asyncio.Queue()
    stack = []
    delay1, delay2, delay3, count = eval(input())
    await asyncio.gather(
        writer(queue, delay1),
        writer(queue, delay2),
        stacker(queue, stack),
        reader(stack, count, delay3))

asyncio.run(main())