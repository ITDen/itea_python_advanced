"""
Создать класс декоратор (DecorTimeCrit) класса. Декоратор, который измеряет время выполнения каждого метода,
и печатает предупреждение, только если время выполнения было больше критического (параметр critical_time)
"""

from time import time, sleep


class DecorTimeCrit:
    """Class decorator"""
    def __init__(self, critical_time):
        self.critical_time = critical_time

    def benchmark(self, func):
        """Benchmark method which calculate method execution time"""
        def wrap(*args, **kwargs):
            start = time()
            func(*args, **kwargs)
            end = time() - start
            if end > self.critical_time:
                print(f'WARNING! {func.__name__} slow. Time = {end} sec.')
            return func
        return wrap

    def __call__(self, cls, *args, **kwargs):
        class Wrapped(cls, *args, **kwargs):
            for attr in dir(cls):
                if not attr.startswith('__') and callable(getattr(cls, attr)):
                    setattr(cls, attr, self.benchmark(getattr(cls, attr)))
        return Wrapped


@DecorTimeCrit(critical_time=2)
class Test:
    def method_1(self, n: int or float):
        print('slow method start')
        sleep(n)
        print('slow method finish')

    def method_2(self, n: int or float):
        print('fast method start')
        sleep(n)
        print('fast method finish')


t = Test()

t.method_1(2)
t.method_2(1)
