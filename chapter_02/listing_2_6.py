""" Выполнение двух сопрограмм """

import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello World!'


async def main() -> None:
    # Приостановить main до возврата из hello_world_message
    message = await hello_world_message()
    # Приостановить main до возврата из add_one
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)


asyncio.run(main())


"""
Код ведет себя как последовательный.
И main, и hello_world приостановлены в ожидании завершения delay(1). 
А когда это случится, main возобновляется и может выполнить add_one
"""