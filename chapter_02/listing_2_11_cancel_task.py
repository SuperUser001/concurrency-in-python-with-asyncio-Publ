""" Снятие задачи """
import asyncio
from asyncio import CancelledError
from util import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    # проверяем состояние задачи
    # done() возвращает True, если задача завершилась
    while not long_task.done():
        print('Задача не закончилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        # Если задача работает дольше 5 с, то мы ее снимаем.
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        # исключение CancelledError может быть возбуждено только внутри предложения await
        await long_task
    except CancelledError:
        print('Наша задача была снята')


asyncio.run(main())

"""
Вызов cancel не прерывает задачу, делающую свое дело;
он снимает ее, только если она уже находится в точке ожидания или
когда дойдет до следующей такой точки
"""