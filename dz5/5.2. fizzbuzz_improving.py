# fizzbuzz from file input
import sys
f = open("D:/Courses/A-level/dz3/fizzbuzz_input.txt")


def fizzbuzz(fizz, buzz, third):
    print(["FB" if i % fizz == 0 and i % buzz == 0 else "B" if i % buzz == 0 else "F" if i % fizz == 0 else i for i in
           range(1, third + 1)])


for numbers in f.readlines():
    line = list(map(lambda i: int(i), numbers.split()))
    fizzbuzz(line[0], line[1], line[2])

f.close()
