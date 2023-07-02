import multiprocessing
import os

# Создание нескольких процессов


def hello_from_process():
    print(f'Привет от дочернего процесса {os.getpid()}!')


if __name__ == '__main__':
    # Сначала создается процесс, при этом
    # передается функция target
    hello_process = multiprocessing.Process(target=hello_from_process)
    # Затем вызывается метод start, чтобы начать выполнение процесса,
    hello_process.start()
    print(f'Привет от родительского процесса {os.getpid()}')
    hello_process.join()
    # метод join, чтобы дождаться завершения процесса