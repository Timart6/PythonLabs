'''
 Дано додатні числа A і B (A> B). На відрізку довжиною A розміщено максимально можлива
кількість відрізків довжиною B (без накладання). Не використовуючи операції множення і ділення,
знайти довжину незайнятої частини відрізка A.
'''


def part_of_sigment(s1, s2):
    while s1 >= s2:
        s1 -= s2

    return s1


def main():
    print("A > B")

    a = float(input("Enter segment length A: "))
    b = float(input("Enter segment length B: "))
    print("Not occupied part of the sigment is ", part_of_sigment(a, b), "cm")


main()
