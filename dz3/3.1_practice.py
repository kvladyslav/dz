# сумма нечетных чисел со списка чисел с 4 до 7 с помощью while
sum = 0
i = 4
while i < 8:
    i += 1
    if i % 2:
        sum += i
    else:
        continue
print(sum)


# сумма нечетных чисел со списка чисел с 3 до 9 с помощью for
sum = 0
for i in range(3, 9):
    if i % 2:
        sum += i
    else:
        continue
print(sum)



# Написать программу, которая выводит сама себя с помощью for
import sys
filename = sys.argv[1]
f = open(filename, 'r')
for line in f:
	print(line)
f.close()


# Написать программу, которая выводит сама себя с помощью f.read()
import sys
filename = sys.argv[1]
f = open(filename, 'r')
print(f.read())
f.close()



# line by line backwards
import sys
filename = sys.argv[1]
f = open(filename)
lines = f.readlines()
for line in reversed(lines):
    print(line)


# all text reversed using while, count and len
import sys
filename = sys.argv[1]
f = open(filename)
text = f.read()
count = len(text)
while count >= 0:
    count -= 1
    print(text[count], end="")
f.close()


# all text reversed using slicing
import sys
filename = sys.argv[1]
f = open(filename)
print(f.read()[::-1])
f.close()


# all text reversed using join(reversed)
import sys
filename = sys.argv[1]
f = open(filename)
text = f.read()
reversed = ''.join(reversed(text))
print(reversed)



# Банкомат выдает сумму максимально возможными купюрами
x = int(input("Введите сумму денег банкомату: "))
for i in (1000, 500, 200, 100, 50, 20, 10, 5, 2, 1):
    if x//i == 0:
        continue
    else:
        print(x//i, "по", i, end=', ')
    x %= i


# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры
amount = int(input("Введите сумму: "))
banknotes = [10, 20, 50, 100, 200, 500, 1000]
limit = 10

for index, nominal in enumerate(banknotes):

    current_limit = limit
    test_sum = current_limit * nominal

    if test_sum <= amount and (index + 1) < len(banknotes):
        while (amount - test_sum) % banknotes[index + 1]:
            test_sum = test_sum - nominal
            current_limit -= 1
        amount -= test_sum
        print(" Take", current_limit, " of ", nominal)
        if amount == 0:
            break
    else:
        current_limit = amount // nominal
        if not (amount % nominal):
            print(" Take", current_limit, " of ", nominal)
            break