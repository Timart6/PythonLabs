'''
16. Дано цілочисельний список, що не містить однакових чисел. Перевірити, чи утворюють його
елементи арифметичну прогресію (A, A + D, A + 2 • D, A + 3 • D, ....). Якщо утворюють, то вивести
різницю прогресії, якщо ні - вивести 0.
'''


def arip_progr(list):
    d = int(list[1]) - int(list[0])
    for i in range(2, len(list)):
        if int(list[i]) is not int(list[0]) + d * i:
            print(0)
            return
    return d


def main():
    numbers = []
    s = int(input("Enter a number\nTo end list just press Enter "))
    while True:
        try:
            numbers.append(s)
            s = int(input("Enter a number\nTo end list just press Enter "))
        except:
            break
    print(arip_progr(numbers))


main()
