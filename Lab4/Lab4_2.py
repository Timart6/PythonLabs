'''
2. Дано рядок, що містить повне ім'я файлу (наприклад, C:\WebServers\home\testsite\www\myfile.txt').
Виділіть з цього рядка ім'я файлу без розширення
'''


def file_name(str):
    location = str.split('\\')
    return location[-1].split('.')[0]


def main():
    name = 'None'
    s = int(input("Do you want to use default file location or your own?\n 1 - default\t 2 - your own"))
    if s == 1:
       name = file_name("C:\WebServers\home\ testsite\www\myfile.txt")
    if s == 2:
       name = input("Print location file")
       name = file_name(name)
    print("File name is ",name)


main()
