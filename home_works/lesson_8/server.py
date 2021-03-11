import socket
from time import time
from math import sqrt
from itertools import count, islice
from io import StringIO

file = StringIO()


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


if __name__ == '__main__':
    prime_list = []
    print(f'Start server...')
    with socket.socket() as sock:
        sock.bind(('0.0.0.0', 9090))
        sock.listen(10)
        while True:
            conn, addr = sock.accept()
            print('connected', addr)
            data = ""
            start = time()
            while True:
                num = conn.recv(4096).decode()
                if not num:
                    break
                data += num
            data = eval(data)
            [file.write(str(num) + '\n') for num in data if is_prime(num)]
            break
    print(f'time: {time() - start}')
    print(f'counter: {len(data)}')
    print(f'======================')
