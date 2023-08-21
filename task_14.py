n = int(input('Введите сравниваемое число: '))
power = 0
while 2 ** power <= n:
    print(2 ** power, end=' ')
    power += 1

