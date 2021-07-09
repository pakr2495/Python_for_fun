
import asyncio

async def func1():
    print("hi function1")
    await asyncio.sleep(2)
    print("function1 completed")
    
async def func2():
    print("hi from function 2")
    await asyncio.sleep(3)
    print("func2 completed")
    
async def func3():
    print("hi from function 3")   
async def main():
    task1 = loop.create_task(func1())
    task2 = loop.create_task(func2())
    task3 = loop.create_task(func3())
    await asyncio.wait([task1,task2,task3])

loop = asyncio.get_event_loop()

loop.run_until_complete(main())

loop.close()