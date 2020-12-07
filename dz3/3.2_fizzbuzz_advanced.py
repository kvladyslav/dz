# Написать fizzbuzz для 20 троек чисел, которые записаны в файл. Читаете из файла первую строку, берете из нее числа,
# считаете для них fizzbuzz, выводите.
import sys
f = open("D:/Courses/A-level/dz3/fizzbuzz_input.txt")
line = f.readline()
while line:
    res = [int(i) for i in line.split() if i.isdigit()]
    fizz = res[0]
    buzz = res[1]
    third = res[2]
    for j in range(1, third + 1):
        if j % fizz == 0 and j % buzz == 0:
            print("FB", end=' ')
        elif j % buzz == 0:
            print("B", end=' ')
        elif j % fizz == 0:
            print("F", end=' ')
        else:
            print(j, end=' ')
        j += 1
    print("\n")
    line = f.readline()
f.close()