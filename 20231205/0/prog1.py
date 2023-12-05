import asyncio
from time import strftime

async def main():
    await(late(3, 'Three'))
    print(f"> {strftime('%X')}")
    await(late(4, "Four"))
    print(f"> {strftime('%X')}")

async def late(delay, msg):
    print(f'Start ({msg})')
    await asyncio.sleep(delay)
    print(msg)

