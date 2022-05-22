'''
1. Описати функцію ArcSin1(X) дійсного типу (X - дійсне , задано в градусах). Скласти
програму розв’язку рівняння sin(ax+b)=c.
'''


from math import sin
from random import uniform


def ArcSin1(X):
    a = round(uniform(-100000, 100000),4)
    b = round(uniform(-100000, 100000),4)

    return sin(a * X + b)


def main():
    x = float(input("Enter real number x: "))
    print("sin(ax + b) =", ArcSin1(x))


main()
