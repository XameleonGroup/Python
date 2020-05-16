import numpy as np
from mat import Mat, MatCalc


def first():
    print('Задание 1')
    print('------------------------------------------------------')
    print('Задать две произвольные матрицы')
    a = Mat(3, 3)
    a = a.random_add()
    b = Mat(3, 3)
    b = b.random_add()
    print('Матрица А:')
    print(a)
    print('\nМатрица B:')
    print(b)
    print('------------------------------------------------------')
    print('\nНайти сумму и разность матриц')
    print('A + B =')
    print(np.add(a, b))
    print('A - B =')
    print(operat.minus(a, b))
    print('------------------------------------------------------')
    print('\nДля матриц вычислить')
    print('Определитель')
    print('Определитель А (|A|)')
    print(round(operat.opr(a), 3))
    print('Определитель B (|B|)')
    print(round(operat.opr(b), 3))
    print('\nТранспонированную матрицу')
    print('Транспонированная А (A^T)')
    print(operat.tran(a))
    print('Транспонированная B (B^T)')
    print(operat.tran(b))
    print('\nОбратную матрицу')
    print('Обратная A (A^-1)')
    revers_a = operat.rever(a)
    print(revers_a)
    print('Проверка: A * A^-1')
    res = operat.dot(a, revers_a)
    print(res)
    print('\nОбратная B (B^-1)')
    revers_b = operat.rever(b)
    print(revers_b)
    print('Проверка: B * B^-1')
    res = operat.dot(a, revers_a)
    print(res)
    print('------------------------------------------------------')
    print('\nЗадать матрицы А(2*2), В(2*3), С(3*2), D(2*1) генератором случайных чисел из интервала [1;10]')
    a = Mat(2, 2).random_add()
    b = Mat(2, 3).random_add()
    c = Mat(3, 2).random_add()
    d = Mat(2, 1).random_add()
    print('Матрица A:')
    print(a)
    print('Матрица B:')
    print(b)
    print('Матрица C:')
    print(c)
    print('Матрица D:')
    print(d)
    print('\nНайти произведения')
    print('A * B =')
    print(operat.dot(a, b))
    print('B * C =')
    print(operat.dot(b, c))
    print('C * B =')
    print(operat.dot(c, b))
    print('C * D =')
    print(operat.dot(c, d))


def second():
    print('------------------------------------------------------')
    print('\nЗадание 2')
    print(
        '\n '
        '/ 3a - 11b + 5c + 4d - 5 = 0\n',
        '/ -8a - 5b - 3c + 10d - 28 = 0\n',
        '\ 3a - b + 5c + 7 = 0\n',
        '\ -6a - 11b + 3c + 12 = 0'
    )

    koff = {
        '1': (3, -11, 5, 4, 5),
        '2': (-8, -5, -3, 10, 28),
        '3': (3, -1, 5, 0, -7),
        '4': (-6, -11, 3, 0, -12),
    }
    print('------------------------------------------------------')
    print('Решить систему линейных уравенений с помощью обратной матрицы')
    m_matrix = transposition(koff, 4)
    rev_matrix = operat.rever(m_matrix)
    data_matrix = transposition(koff, 4, 4)
    answer = operat.dot(rev_matrix, data_matrix)
    a, b, c, d = round(answer[0][0], 1), round(answer[1][0], 1), round(answer[2][0], 1), round(answer[3][0], 1)
    print(f'Ответ: a = {a}, b = {b}, c = {c}, d = {d}')
    print('------------------------------------------------------')
    print('\nРешить систему линейных уравенений методом Крамера')
    m_matrix = transposition(koff, 4)
    m_a = transposition(koff, 0)
    m_b = transposition(koff, 1)
    m_c = transposition(koff, 2)
    m_d = transposition(koff, 3)
    oper = operat.opr(m_matrix)
    oper_a = operat.opr(m_a)
    oper_b = operat.opr(m_b)
    oper_c = operat.opr(m_c)
    oper_d = operat.opr(m_d)
    a = round(oper_a / oper, 1)
    b = round(oper_b / oper, 1)
    c = round(oper_c / oper, 1)
    d = round(oper_d / oper, 1)
    print(f'Ответ: a = {a}, b = {b}, c = {c}, d = {d}')
    print('------------------------------------------------------')
    print('Проверка:')
    print(3*a - 11*b + 5*c + 4*d - 5,'= 0')
    print(-8*a - 5*b - 3*c + 10*d - 28,'= 0')
    print(3*a - b + 5*c + 7,'= 0')
    print(-6*a - 11*b + 3*c + 12,'= 0')


def transposition(koff, l, test=None):
    matrix = []
    for i in koff.values():
        checked = list(i)
        checked[l] = checked[4]
        if test:
            matrix.append(checked[test])
        else:
            matrix.append(checked[:4])
    if test:
        matrix = Mat(4, 1).data_add(matrix)
    else:
        matrix = Mat(4, 4).data_add(matrix)
    return matrix

operat = MatCalc()
first()
second()
