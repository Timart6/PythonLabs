'''
11. Дано список. Вивести спочатку всі негативні елементи, а потім всі інші.
'''


def print_neg(list):
    pos = []
    for num in list:
        if num < 0: print(num)
        elif num > 0: pos.append(num)
    for num in pos:
        print(num)


def main():
    s = float(input("Enter number\nIf you want to end list, just press enter "))
    numbers = []
    while True:
        try:
            numbers.append(s)
            s = float(input())
        except:
            break
    print_neg(numbers)


main()
