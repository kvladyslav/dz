# Переделать вторую задачу так, чтобы результат писался в другой файл.
import sys
f = open("D:/Courses/A-level/dz3/fizzbuzz_input.txt")
f2 = open('D:/Courses/A-level/dz3/fizzbuzz_output.txt', 'w')
line = f.readline()
while line:
    res = [int(i) for i in line.split() if i.isdigit()]
    fizz = res[0]
    buzz = res[1]
    third = res[2]
    for j in range(1, third + 1):
        if j % fizz == 0 and j % buzz == 0:
            f2.write("FB ")
        elif j % buzz == 0:
            f2.write("B ")
        elif j % fizz == 0:
            f2.write("F ")
        else:
            f2.write(str(j) + " ")
        j += 1
    f2.write("\n")
    line = f.readline()
f.close()
f2.close()