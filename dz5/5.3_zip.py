# Задание 3 для подсчета частоты слов в файле с ипспользование map и лямбды
f = open("D:/Courses/A-level/dz5/eng.txt", "r")
words = f.read().split()
print(dict(zip(words, list(map(lambda word: words.count(word), words)))))
f.close()


