'''
1. Дано рядок. Вивести окремі слова, що входять до нього, розділені пробілами, впорядкованими за
алфавітом, в стовпчик.
'''


def sort(str):
    str = str.lower()
    words = str.split(" ")
    words.sort()
    for word in words:
        print(word)


def main():
    string = input("Enter a string")
    sort(string)
main()
