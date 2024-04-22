print('введите возраст в месяцах: ')
month = int(input())

years = month // 12
month %= 12

print('лет:', years, '\nмесяцев:', month)
      