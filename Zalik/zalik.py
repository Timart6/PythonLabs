'''
Завдання #1 - Назви та ПІП керівників в файл rectors.csv
Завдання №2 - З роком заснування між 1950 та 1999
'''


import requests
import csv


def get_region():   #Функция что получает от пользователя код и возвращает его и университет, что хранился по этому коду
    regions = ["01", "05", "07", "12", "14", "18", "21", "23", "26", "32", "35", "44", "46", "48", "51",
    "53", "56", "59", "61","63", "65", "68", "71", "73", "74", "80", "85"]
    code = input("Enter a region code ")
    if code in regions == False:
        print("This code doesn't exist")
        return 0
    r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=' + code + '&exp=json')
    universities: list = r.json()
    return (universities,code)


def save_all_info():
    (universities,region) = get_region()
    # Получение данных от функции_get region для дальнейшей работы с ними,
    # есть во всех остальных функциях
    with open('universities.csv', mode='w',encoding='CP1251') as f:      #Сохранение данных в universities.csv
        writer = csv.DictWriter(f, fieldnames=universities[0].keys())
        writer.writeheader()
        writer.writerows(universities)
    with open('universities' + region + '.csv', mode='w',encoding='CP1251') as f:     #Сохранение данных в universities<region>.csv
        writer = csv.DictWriter(f, fieldnames=universities[0].keys())
        writer.writeheader()
        writer.writerows(universities)


def name_filter():             #Функция фильтрует данные и достает только имя заведения, пост ректора и его ФИО
    (universities,region) = get_region()
    filtered_data = [{k: row[k] for k in ['university_name','university_director_post','university_director_fio']}
    for row in universities]
    with open('rectors.csv' + region + '.csv', mode='w', encoding='CP1251') as f:
        writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
        writer.writeheader()
        writer.writerows(filtered_data)


def name_1950_1999_filter():
    (universities,region) = get_region()
    # Функция предоставляет выбор - сохранить данные о всех заведениях с 1950 до 1999 или
    # о заведениях открытых в указанным пользователем году
    year = int(input("Enter 0 if you want all universities,if specific enter a year"))
    if (year == 0):
       filtered_data = [{k: row[k] for k in ['registration_year','university_name','university_director_post',
       'university_director_fio']} for row in
       list(filter(lambda x: 1999 > int(x['registration_year'] or 0) > 1950, universities))]
       with open('rectors_1950-1999.csv' + region + '.csv', mode='w', encoding='CP1251') as f:
          writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
          writer.writeheader()
          writer.writerows(filtered_data)
    if (year > 1949 and year < 2000):
        filtered_data = [{k: row[k] for k in ['registration_year','university_name', 'university_director_post',
        'university_director_fio']} for row in
        list(filter(lambda x: int(x['registration_year'] or 0) == year, universities))]
        with open('rectors_' + str(year) + '.csv' + region + '.csv', mode='w', encoding='CP1251') as f:
            writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
            writer.writeheader()
            writer.writerows(filtered_data)
    elif(year!=0):
        print("You enter wrong year")


def main():
    #Выбор действия
    s = int(input("What info you want to get?\n1 - all data\t2 - all rector names\t3 - rector names 1950 - 1999\n"))
    if s == 1:
        save_all_info()
    if s == 2:
        name_filter()
    if s == 3:
        name_1950_1999_filter()
    if (s > 3 or s < 1):
        print("Wrong command")


main()
