# Задание 3
f = open("D:/Courses/A-level/dz5/eng.txt", "r")
frequency_dict = {}


def freq(word):
    if word in frequency_dict:
        frequency_dict[word] += 1
    else:
        frequency_dict[word] = 1


list(map(freq, f.read().split()))
# sort = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)  # отсортировать по уменьшению частоты слов
print(frequency_dict)
# print(sort)  # отсортированный frequency_dict
f.close()


# With a help of reduce
# f = open("D:/Courses/A-level/dz5/eng.txt", "r")
# from functools import reduce
# print(reduce(lambda d, c: d.update([(c, d.get(c, 0)+1)]) or d, f.read().split(), {}))
# f.close()












