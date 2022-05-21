'''
6. Дано рядок. Якщо в цьому рядку буква f зустрічається тільки один раз, виведіть її індекс. Якщо
вона зустрічається два і більше разів, виведіть індекси її першої і останньої появи. Якщо буква f в
цьому рядку не зустрічається, нічого не виводьте.
'''


def f_check(str):
    number = [0,0]
    i = 0
    for lett in str:
        i+=1
        if lett == 'f' or lett == 'F':
            if number[0] == 0: number[0] = i
            else: number[1] = i
    if number[0] != 0:
        if number[1] != 0: print("First appearance: ",number[0],"Last appearance: ",number[1])
        else: print("Only appearance: ",number[0])


def main():
    string = input("Input word")
    f_check(string)


main()
