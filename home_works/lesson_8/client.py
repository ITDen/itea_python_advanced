import socket
from time import time
from math import sqrt
from itertools import count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


if __name__ == '__main__':
    prime_list = [i for i in range(2000000 + 1) if is_prime(i)]
    prime_len = len(prime_list)
    start = time()
    with socket.socket() as sock:
        sock.connect(('127.0.0.1', 9090))
        sock.send(str(prime_list).encode())
    print(f'time: {time() - start}')
    print(f'counter: {prime_len}')
    print(f'======================')
