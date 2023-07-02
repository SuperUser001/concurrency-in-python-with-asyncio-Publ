"""
Создание многопоточного Python-приложения

Процессы могут порождать дополнительные потоки, разделяющие
память со своим процессом-родителем. Они могут конкурентно вы-
полнять другую работу, это называется многопоточностью.
"""
import threading


def hello_from_thread():
    # метод, печатающий имя текущего потока
    print(f'Привет от потока {threading.current_thread()}!')


hello_thread = threading.Thread(target=hello_from_thread)
# *target* is the callable object to be invoked by the run()

# метод потока start, запускающий поток
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name
"""
    Return the current Thread object, corresponding to the caller's thread of control.
    If the caller's thread of control was not created through the threading
    module, a dummy thread object with limited functionality is returned.
"""
print(f'В данный момент Python выполняет {total_threads} поток(ов)')
print(f'Имя текущего потока {thread_name}')
hello_thread.join()
# метод join, который приостанавливает программу, до тех
# пор пока указанный поток не завершится
""" 
    This blocks the calling thread until the thread whose join() method is
    called terminates -- either normally or through an unhandled exception
     or until the optional timeout occurs.
"""

"""
Процесс C { Память: главный потом, рабочий поток, рабочий поток }
"""