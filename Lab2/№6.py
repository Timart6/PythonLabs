'''
6. Дано ціле число в діапазоні 1-7. Вивести рядок - назва дня тижня, що відповідає даному числу (1 -
«понеділок», 2 - «вівторок» і т. д.)
'''


def dayofweek(a: int) -> str:
    if a == 1:
        return 'Понеділок'
    if a == 2:
        return 'Вівторок'
    if a == 3:
        return 'Середа'
    if a == 4:
        return 'Четвер'
    if a == 5:
        return 'П`ятниця'
    if a == 6:
        return 'Суббота'
    if a == 7:
        return 'Неділя'
    if a < 1 or a > 7:
        return 'Ви ввели не те число'


x = int(input('Введіть число'))
result = dayofweek(x)
print(result)
