""" Выполнение кода, пока другие операции работают в фоне """
import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код..")


async def main():
    first_delay = asyncio.create_task(delay(4))
    second_delay = asyncio.create_task(delay(3))
    # даже во время выполнения длительных операций наше приложение
    # может выполнять другие задачи.
    await hello_every_second()
    await first_delay
    await second_delay


asyncio.run(main())
