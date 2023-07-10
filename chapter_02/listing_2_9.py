""" Конкурентное выполнение нескольких задач """
import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


# КОНКУРЕНТНОСТЬ ЗАДАЧ: ЗАДАЧИ НЕ ВЫПОЛНЯЮТСЯ КОНКУРЕНТНО
# КОНКУРЕНТНО ЗАДАЧИ ТОЛЬКО СПЯТ
async def main():
    # в точке,где встречается первое после создания задачи предложение await, все
    # ожидающие задачи начинают выполняться, так как await запускает
    # очередную итерацию цикла событий
    # т.е. все три задачи начинают выполняться и засыпают одновременно.
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await sleep_for_three
    await sleep_again
    await sleep_once_more


asyncio.run(main())

"""
Здесь мы запустили три задачи, каждой из которых для завершения
нужно 3 с. Каждое обращение к create_task возвращает управление
немедленно, поэтому до предложения await sleep_for_three мы до-
ходим сразу же.
"""


