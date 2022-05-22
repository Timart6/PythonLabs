'''
1. Описати функцію IsPrime (N) логічного типу, яка повертає True, якщо цілий
параметр N (> 1) є простим числом, і False в іншому випадку (число, більше 1,
називається простим, якщо воно не має позитивних дільників, крім 1 і самого себе).
Дано набір з 10 цілих чисел, більших 1. За допомогою функції IsPrime знайти
кількість простих чисел в даному наборі.
'''


def IsPrime(N):
    if N > 1:
        for i in range(2,N-1):
            if N % i == 0:
               return False
        return True
    else: return False


def main():
    numbers = [None] * 10
    i = 1
    while i < 11:
        numbers[i-1] = int(input("Enter number "))
        i+=1
    for n in numbers:
        print(n," ",IsPrime(n))


main()
