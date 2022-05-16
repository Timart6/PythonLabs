'''
Дано число A (> 1). Вивести найменше з цілих чисел K, для яких сума 1 + 1/2 + … + 1/K будет
більше A, і саму цю суму.
'''


def smallest_k(num):
    k = 3
    while True:
        sum = 0
        for i in range(1, k):
            sum = sum + 1 / i

        if sum > num:
            print("Number:", k, "Sum:", sum)
            break
        else:
            k += 1


def main():
    a = int(input("Enter integer A (A > 1): "))
    smallest_k(a)


main()
