arr = ['2','3','3','2','2','5','3','3','3','3','4','5','4','4','3','5','5','5','2','5','5','2']
number2 = 0
number3 = 0
number4 = 0
number5 = 0
for i in range(len(arr)):
    if  arr[i] == '2':
        number2 += 1
    elif  arr[i] == '3':
        number3 += 1
    elif  arr[i] == '4':
        number4 += 1
    elif  arr[i] == '5':
        number5 += 1
print('количество пятерок:', number5)
print('количество четверок:', number4)
print('количество троек:', number3)
print('количество двоек:', number2)