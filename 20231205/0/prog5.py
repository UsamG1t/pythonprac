import asyncio

async def snd(evsnd):
    evsnd.set()
    print('snd: generated evsnd')

async def mid1(evsnd, evmid1):
    await evsnd.wait()
    print('mid1: recieved evsnd')
    evmid1.set()
    print('mid1: generated evmid1')

async def mid2(evsnd, evmid2):
    await evsnd.wait()
    print('mid2: recieved evsnd')
    evmid2.set()
    print('mid2: generated evmid2')

async def rcv(evmid1, evmid2):
    await asyncio.gather(
        evmid1.wait(),
        evmid2.wait())
    print('rcv: recieved evmid1/evmid2')
    
async def main():
    evsnd, evmid1, evmid2 = asyncio.Event(), asyncio.Event(), asyncio.Event()
    await asyncio.gather(
        snd(evsnd),
        mid1(evsnd, evmid1),
        mid2(evsnd, evmid2),
        rcv(evmid1, evmid2))

asyncio.run(main())