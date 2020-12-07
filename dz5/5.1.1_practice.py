# Задание 1
# Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.
# После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")
test = [text1, text2]


def up(text):
    return text.upper()


def low(text):
    return text.lower()


rows1 = list(map(up, test))
rows2 = list(map(low, test))

print(rows1)
print(rows2)






