import asyncio
from time import strftime

async def main():
    res = await asyncio.gather(
        late(3, 'Three'),
        late(1, "One"),
        late(2, "Two"))
    print(res)

async def late(delay, msg):
    print(f'Start ({msg})')
    await asyncio.sleep(delay)
    print(msg)
    print(f"> {strftime('%X')}")
    return delay
