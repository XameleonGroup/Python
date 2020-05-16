import numpy as np


class Mat:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = np.zeros((self.n, self.m), dtype=int)

    def random_add(self):
        self.matrix = np.random.randint(1, 11, (self.n, self.m), dtype=int)
        return self.matrix

    def data_add(self, ar):
        for i in range(len(ar)):
            self.matrix[i] = ar[i]
        return self.matrix

    def display(self):
        print(self.matrix)


class MatCalc:

    @staticmethod
    def minus(a, b):
        b = MatCalc.dot(-1, b)
        return np.add(a, b)

    @staticmethod
    def dot(a, b):
        return np.dot(a, b)

    @staticmethod
    def opr(a):
        return np.linalg.det(a)

    @staticmethod
    def tran(a):
        return np.transpose(a)

    @staticmethod
    def rever(a):
        return np.linalg.inv(a)