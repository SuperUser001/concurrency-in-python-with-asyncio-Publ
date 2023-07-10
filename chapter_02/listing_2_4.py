""" Использование await для ожидания результата
сопрограммы """

import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    # Приостановиться и ждать результата add_one(1)
    one_plus_one = await add_one(1)
    # Приостановиться и ждать результата add_one(2)
    two_plus_one = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)


asyncio.run(main())

""" 
По сути, код работает так же, как и обычный последовательный код.
Это имитация обычного стека вызовов.
"""
