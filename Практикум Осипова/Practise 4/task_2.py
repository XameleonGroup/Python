import numpy
from sympy import symbols, diff

def f(x):
    return 7 / (12 - x - x ** 2)



def main():
    x = numpy.linspace(-20, 20, 500)
    y = numpy.array(f(x))
