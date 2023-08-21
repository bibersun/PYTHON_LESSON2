n = int(input('Введите количество монет: '))
count = 0
for i in range(n):
    count += 1 if int(input(f'Введите состояние монеты {i + 1}, 0-решка, 1 - орел: ')) == 0 else 0
print(f'Количество решек равно {count}')