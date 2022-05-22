'''
1. Описати функцію Power1 (A, B) дійсного типу, яка знаходить величину A^B
за формулою A^B = exp (B ln (A)) (параметри A і B - дійсні). У разі нульового або
негативного параметра A функція повертає 0. З допомогою цієї функції знайти
степені AP, BP, CP, якщо дано числа P, A, B, C.
'''


from math import exp
from math import log
from math import e


def Power1 (A,B):
    if B < 1:
       return 0
    A = exp(B * log(A, e))
    return A


def main():
    A = float(input("Enter A "))
    B = float(input("Enter B "))
    C = float(input("Enter C "))
    P = float(input("Enter P "))
    print("A^P ",Power1(A,P))
    print("B^P ",Power1(B,P))
    print("C^P ",Power1(C,P))


main()
