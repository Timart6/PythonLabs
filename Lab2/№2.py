# 2. Дано три цілих числа. Знайти кількість додатних чисел в початковому наборі.


def positive(a, b, c):
    i = 0
    if a > 0:
        i = i+1
    if b > 0:
        i = i+1
    if c > 0:
        i = i+1
    return i


a1 = int(input('Enter first number'))
b1 = int(input('Enter second number'))
c1 = int(input('Enter thirst number'))
result = positive(a1, b1, c1)
print('Amount of positive numbers: ', result)
