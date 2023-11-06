# Когда вызывается функция slow_function,
# декоратор timing_decorator измеряет время,
# которое ушло на её выполнение, и выводит это время в консоль
import functools
from time import time, sleep


# Декоратор для логирования
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"*log_decorator: Вызвана функция {func.name} с аргументами {args} и ключевыми аргументами {kwargs}.")
        # Вызов оборачиваемой функции
        result = func(*args, **kwargs)
        print(f"*log_decorator: Функция {func.name} вернула {result}.")
        return result

    return wrapper


# Декоратор для измерения времени выполнения функции
def timing_decorator(func):
    # @log_decorator  # Применение декоратора внутри декоратора
    def wrapper(*args, **kwargs):
        print(f"#timing_decorator: Вызвана функция {func.name}")
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"#timing_decorator: Функция {func.name} выполнилась за {elapsed_time:.6f} секунд.")
        return result

    return wrapper


@timing_decorator
@log_decorator
def slow_function(duration):
    print(f">>>slow_function: Вызвана функция с параметром {duration}.")
    sleep(duration)
    return duration


if __name__ == '__main__':
    slow_function(1)
