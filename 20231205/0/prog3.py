import asyncio

async def squarer(param):
    return param**2

async def doubler(param):
    return param*2

async def main(x, y):
    x, y = await asyncio.gather(squarer(x), squarer(y))
    x, y = await asyncio.gather(doubler(x), doubler(y))
    print(x, y)

asyncio.run(main(*(eval(input()))))