fizz = int(input('Введите число fizz: '))
buzz = int(input('Введите число buzz: '))
third = int(input('Введите третье число: '))
for i in range(1, third + 1):
    if i % fizz == 0 and i % buzz == 0:
        print("FB", end=' ')
    elif i % buzz == 0:
        print("B", end=' ')
    elif i % fizz == 0:
        print("F", end=' ')
    else:
        print(i, end=' ')
    i += 1