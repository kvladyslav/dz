# таблица Пифагора
# for i in range(1, 10):
#     l = [i * j for j in range(1, 10)]
#     print(l)



# Ввести число, вывести все его делители
# x = int(input("Введите число: "))
# x = [i for i in range(1, x + 1) if not x % i]
# print(x)



# fizzbuzz with list comprehension
fizz = int(input('Введите число fizz: '))
buzz = int(input('Введите число buzz: '))
x = int(input('Введите третье число: '))
Z = ["FB" if i % fizz == 0 and i % buzz == 0 else "B" if i % buzz == 0 else "B" if i % fizz == 0 else i for i in
     range(1, x + 1)]
print(Z)



# Банкомат выдает сумму максимально возможными купюрами
x = int(input("Введите сумму денег банкомату: "))
banknotes = []
for i in [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]:
    if x//i:
        banknotes.append(str(x // i) + " по " + str(i))
    x %= i
print(banknotes)



# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры
amount = int(input("Введите сумму: "))
banknotes = [10, 20, 50, 100, 200, 500, 1000]
limit = 10
result = []

for index, nominal in enumerate(banknotes):

    current_limit = limit
    test_sum = current_limit * nominal

    if test_sum <= amount and (index + 1) < len(banknotes):
        while (amount - test_sum) % banknotes[index + 1]:
            test_sum = test_sum - nominal
            current_limit -= 1
        amount -= test_sum
        result.append("Take " + str(current_limit) + " of " + str(nominal))
        if amount == 0:
            break
    else:
        current_limit = amount // nominal
        if not (amount % nominal):
            result.append("Take " + str(current_limit) + " of " + str(nominal))
            break
print(result)



# fizzbuzz from file input
import sys
f = open("D:/Courses/A-level/dz3/fizzbuzz_input.txt")
line = f.readline()
while line:
    res = [int(i) for i in line.split() if i.isdigit()]
    z = ["FB" if i % res[0] == 0 and i % res[1] == 0 else "B" if i % res[1] == 0 else "F" if i % res[0] == 0 else i for
         i in range(1, res[2] + 1)]
    print(z)
    line = f.readline()
f.close()



# fizzbuzz from file input to file output
import sys
f = open("D:/Courses/A-level/dz3/fizzbuzz_input.txt")
f2 = open('D:/Courses/A-level/dz3/fizzbuzz_output.txt', 'w')
line = f.readline()
while line:
    res = [int(i) for i in line.split() if i.isdigit()]
    Z = ["FB" if i % res[0] == 0 and i % res[1] == 0 else "B" if i % res[1] == 0 else "B" if i % res[0] == 0 else i for
         i in range(1, res[2] + 1)]
    listToStr = ' '.join([str(elem) for elem in Z])
    f2.write(listToStr + '\n')
    line = f.readline()
f.close()
f2.close()