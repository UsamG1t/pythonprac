import asyncio
from queue import Queue

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()

    i1, i2 = start, middle
    for j in range(start, finish):
        if i1 == middle:
            B[j] = A[i2]
            i2 += 1
        elif i2 == finish:
            B[j] = A[i1]
            i1 += 1
        else:
            if A[i1] < A[i2]:
                B[j] = A[i1]
                i1 += 1
            else:
                B[j] = A[i2]
                i2 += 1
    event_out.set()

async def mtasks(A):
    Ac = A.copy()
    tasks = []
    events = []
    start_event = asyncio.Event()
    for i in range(len(A)):
        events.append(start_event)
    start_event.set()
    
    event_step = 0
    i = 1
    count = 1
    B = [0]*len(A)
    while i < len(A):
        Array_in = Ac if count % 2 else B
        Array_out = B if count % 2 else Ac
        for j in range(0,len(A),i * 2):
            start = j
            middle = j + i if len(A) - 1 > j + i else len(A) - 1
            finish = j + 2*i if len(A) > j + 2 * i else len(A)
            tmp = asyncio.Event()
            
            tasks.append(asyncio.create_task(merge(Array_in, Array_out, start,\
                middle, finish, events[event_step], events[event_step + 1], tmp) ) )
            events.append(tmp)
            event_step += 2
   
        events.append(events[-1])
        i *= 2
        count = 1 - count

    return (tasks, Ac if count % 2 else B)

import sys
exec(sys.stdin.read())