while True:
    try:
        n = int(input('Введите количество чисел: '))
        if n < 0:
            print('Вы ввели не число, попробуйте еще раз: ')
        else:
            break
    except:
        print('Вы ввели не число, попробуйте еще раз: ')
        
i = 0
num = []
while i < n:
    s = input('Введите новое двоичное число: ')
    flag = True
    for c in s:
        flag = flag and (c in '-01')
    if flag and s != '-':
        num.append(s)
        i += 1
    else:
        print('Вы ввели не двоичное число! Попробуйте еще раз')
    
print(f'{"Двоичное":^25}{"Десятичное":^13}')
for i in range(n):
    if num[i][0] == '-':
        num[i] = num[i][1:]
        print(f'{num[i]:^25}{-int(num[i], 2):^13}')
    else:
        print(f'{num[i]:^25}{int(num[i], 2):^13}')