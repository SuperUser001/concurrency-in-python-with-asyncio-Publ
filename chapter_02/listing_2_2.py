""" Сравнение сопрограмм с обычными функциями """


async def coroutine_add_one(number: int) -> int:
    return number + 1


def add_one(number: int) -> int:
    return number + 1


function_result = add_one(1)
# сопрограммы не выполняются, если их вызвать напрямую
# возвращается объект сопрограммы, который будет выполнен позже.
# Чтобы выполнить сопрограмму, ее надо передать ее циклу событий.
coroutine_result = coroutine_add_one(1)
print(f'Результат функции равен {function_result}, а его тип равен {type(function_result)}')
print(f'Результат сопрограммы равен {coroutine_result}, а его тип равен {type(coroutine_result)}')
