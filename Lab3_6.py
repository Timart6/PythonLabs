'''
Логічній змінній t присвоїти значення true або false залежно від того, є натуральне число k
ступенем 3 чи ні.
'''


def power_3(num):
    while num > 1:
        num /= 3

    if num == 1:
        t = True
    else:
        t = False

    return t


def main():
    n = int(input("Enter natural number: "))
    print("Is the power of number three?", power_3(n))


main()