"""
1. Программа принимает от пользователя диапазоны для коэффициентов a, b, c квадратного уравнения: ax2 + bx + c = 0.
Перебирает все варианты целочисленных коэффициентов в указанных диапазонах,
определяет квадратные уравнения, которые имею решение

Пример выполнения:

a1: -2
a2: 2
b1: -3
b2: 1
c1: 0
c2: 4
"""


def square_equation(a_input_range=(), b_input_range=(), c_input_range=()):
    a_range = [num for num in range(a_input_range[0], a_input_range[1] + 1)]
    b_range = [num for num in range(b_input_range[0], b_input_range[1] + 1)]
    c_range = [num for num in range(c_input_range[0], c_input_range[1] + 1)]

    for a in a_range:
        for b in b_range:
            for c in c_range:
                if a == 0:
                    continue
                d = b ** 2 - 4 * a * c
                if d > 0:
                    import math
                    x1 = (-b + math.sqrt(d)) / (2 * a)
                    x2 = (-b - math.sqrt(d)) / (2 * a)
                    print(f'a = {a}, b = {b}, c = {c}, discr = {d}, YES x1 = {x1}, x2 = {x2}')
                elif d == 0:
                    x = -b / (2 * a)
                    print(f'a = {a}, b = {b}, c = {c}, discr = {d}, YES x = {x}')
                else:
                    print(f'a = {a}, b = {b}, c = {c}, discr = {d}, NO')
                print('============================================')


square_equation(a_input_range=(-2, 2), b_input_range=(-3, 6), c_input_range=(0, 4))
# ==============================================================================================================

"""
2. Дана матрица целых чисел 10x10. Вводится число. Выяснить, какие строки и столбцы матрицы содержат данное число.
(либо рандом либо чтение из файла (input.txt))
"""


def num_finder(number):
    try:
        number = int(number)
    except ValueError:
        print('Wrong input! You should enter a number!')
        return
    else:
        try:
            with open('input.txt') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print('File not found!')
            return
        else:
            try:
                matrix = [list(map(int, line.strip('\n').split())) for line in lines]
            except ValueError:
                print('Wrong data in file!')
                return
            else:
                if not matrix:
                    print('File is empty!')
                    return
                row_entries = []
                column_entries = []
                for row_idx, row_value in enumerate(matrix):
                    for column_idx, column_value in enumerate(row_value):
                        if column_value == number:
                            row_entries.append(row_idx)
                            column_entries.append(column_idx)
                if row_entries:
                    print(f'Rows (index): {", ".join(map(str, row_entries))}\n'
                          f'Columns (index): {", ".join(map(str, column_entries))}')
                else:
                    print('No entries!')


num_finder(22)
