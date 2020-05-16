import math

def f_1(x):
    return x * math.tan(x ** 2 + 1)


def f_2(x):
    return 1 / (1 + math.log(x))


def type_trapeze(f, a, b, n=500):
    h = (b - a) / n
    return (sum([f(a + i * h) for i in range(1, n)]) + (f(a) + f(b)) / 2) * h


def formula_simpson(f, a, b, n=500):
    h = (b - a) / (2 * n)
    return (f(a) + f(b) + 4 * sum([f(a + i * h) for i in range(1, n*2) if i%2 == 1]) +
            2 * sum([f(a + i * h) for i in range(1, n*2-1) if i % 2 == 0])) * h/3


def main():
    print('∫(x * tg(x^2 + 1))dx, x=[0, 0.5]')
    print('Округленный результат, полученный методом трапеции:',
          round(type_trapeze(f_1, 0, 0.5), 7))
    print('Округленный результат, полученный методом Симпсона:',
          round(formula_simpson(f_1,0,0.5), 7))
    print('∫(1/(1 +ln(x)))dx, x=[1, π]')
    print('Округленный результат, полученный методом трапеции:',
          round(type_trapeze(f_2, 1, math.pi), 7))
    print('Округленный результат, полученный методом Симпсона:',
          round(formula_simpson(f_2, 1, math.pi), 7))


if __name__ == '__main__':
    main()

