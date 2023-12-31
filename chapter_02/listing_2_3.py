""" Выполнение сопрограммы: вспомогательная функция asyncio.run, которую
можно использовать для запуска нашей сопрограммы """
import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1

# asyncio.run  создает новое событие
# Потом она выполняет код переданной нами сопрограммы до конца и возвращает результат.
# в конце она останавливает и закрывает цикл событий
result = asyncio.run(coroutine_add_one(1))
print(result)

""" 
asyncio.run – задумана как главная точка входа в созданное нами 
приложение asyncio. Она выполняет только одну сопрограмму, и эта сопрограмма должна по-
заботиться обо всех остальных аспектах приложения.
"""