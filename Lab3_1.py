'''
Підрахувати k - кількість цифр в десятковому запису цілого невід'ємного числа n
'''


def num_of_digit(n):
    k = 0
    while n / 10 != 0:
        n //= 10
        k += 1

    return k


def main():
    num = int(input("Enter positive integer: "))
    print("Number of digits:", num_of_digit(num))


main()