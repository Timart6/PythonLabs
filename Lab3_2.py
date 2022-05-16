'''
Визначити, чи є задане натуральне число досконалим, тобто рівним сумі всіх своїх дільників, крім
самого цього числа (наприклад, число 6 досконале: 6 = 1 + 2 + 3)
'''


def perfect(num):
    sum = 0

    for i in range(1, num - 1):
        if num % i == 0:
            sum += i

    if sum == num:
        print("Number is perfect")
    else:
        print("Number isn't perfect")


def main():
    n = int(input("Enter natural number: "))

    perfect(n)


main()
