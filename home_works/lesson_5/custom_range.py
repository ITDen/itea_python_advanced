'''
Реализовать класс - аналог Range
'''


class CustomRange:
    def __init__(self, *args, **kwargs):
        """
        Custom range class
        :param args: CustomRange(stop), CustomRange(start, stop) or CustomRange(start, stop, step)
        :param kwargs:
        """
        if not args:
            raise ValueError('Should set at least 1 param!')
        self._start = args[0] if len(args) > 1 else 0
        self._stop = args[0] if len(args) == 1 else args[1]
        self._step = args[2] if len(args) > 2 else 1

    def __iter__(self):
        while self._start < self._stop:
            yield self._start
            self._start += self._step


test = iter(CustomRange(5))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print('============')

for i in CustomRange(0, 10, 2):
    print(i)
print('============')
