'''
1. Описати функцію PowerA3 (A, B), яка обчислює третю ступінь числа A і повертає її в
змінну B (A - вхідний, B - вихідний параметр; обидва параметри є дійсними). За
допомогою цієї функції знайти треті ступені п'яти даних чисел.
'''


def PowerA3(A):
    return A*A*A


def main():
    a = float(input("Enter A "))
    b = PowerA3(a)
    print("B: ",b)


main()
