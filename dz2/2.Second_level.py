# Проверить, является ли число четным, делится ли на 4 и на 6 одновременно, но так, чтоб не делилось на 5
x = int(input("Введите число: "))
if x % 2 == 0 and x % 4 == 0 and x % 6 == 0 and x % 5 != 0:
    print("Ok")
else:
    print("Not ok")


#Ввести число, вывести сумму его делителей:
x = int(input("Введите число: "))
sum = 0
for i in range(1, x+1):
    if x % i == 0:
        sum += i
print(sum)


#Ввести число, вывести все его нечетные делители:
x = int(input("Введите число: "))
for i in range(1, x+1):
    if x % i == 0:
        if i % 2:
            print(i)


#Ввести число, вывести делители произведения делителей числа
x = int(input("Введите число: "))
pr = 1
for i in range(1, x+1):
    if x % i == 0:
        pr *= i
for j in range(1, pr+1):
    if pr % j == 0:
        print(j)