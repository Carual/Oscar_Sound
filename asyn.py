import asyncio


async def main():
    task = asyncio.create_task(other_function())
    print("A")
    print("B")
    await asyncio.sleep(2)


async def other_function():
    print("1")
    print("2")
asyncio.run(main())
