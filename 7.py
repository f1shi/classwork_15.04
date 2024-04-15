month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print('введите порядковый номер месяца:')
monthN = int(input())
print('введите число:')
dayM = int(input())

if dayM - 1 > 0 and daysOfMonth[monthN - 1] >= dayM + 1:
    print('преведуший день:', dayM - 1)
    print('следующий день:', dayM + 1)
elif dayM - 1 < 0:
    print('преведуший день:', daysOfMonth[monthN - 2])
    print('следующий день:', dayM + 1)
elif dayM + 1 > daysOfMonth[monthN - 1]:
    print('преведуший день:', dayM - 1)
    print('следующий день: 1', )
