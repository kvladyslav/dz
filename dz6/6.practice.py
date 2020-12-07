# 1. Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

from statistics import mean
students = {
    'Andry Gordon': [10, 9, 10, 8, 10, 8, 9, 4, 9],
    'Vladyslav Kurpiianov': [10, 10, 10, 8, 10, 8, 9, 4, 9],
    'Michael Shrimp': [7, 9, 8, 7, 10, 8, 9, 4, 4],
    'John Bampty': [6, 9, 9, 9, 9, 9, 1, 2, 5],
    'Aliston Midy': [10, 8, 9, 4, 9, 5, 9, 7, 3]}

most_value = round(mean(max(students.items(), key=lambda x: mean(x[1]))[1]), 2)
most_key = max(students.items(), key=lambda x: mean(x[1]))[0]
least_value = round(mean(min(students.items(), key=lambda x: mean(x[1]))[1]), 2)
least_key = min(students.items(), key=lambda x: mean(x[1]))[0]

print('The most successful - ', most_key, ' with ', most_value)
print('The least successful - ', least_key, ' with ', least_value)


# 2. Создать структуру данных для студентов из имен и фамилий, можно случайных. Придумать структуру данных, чтобы
# указывать, в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java).
# Студент может учиться в нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

students = {
    'Andry Gordon': ['Python', 'Java'],
    'Vladyslav Kupriianov': ['Python', 'FullStack', 'Java'],
    'Michael Shrimp': ['Java'],
    'John Bampty': ['FullStack', 'Java'],
    'Aliston Midy': ['FrontEnd']}

print('Students in two or more groups: ', [key for key, val in students.items() if len(val) >= 2])
print("Students who don't study FrontEnd: ", [key for key, val in students.items() if 'FrontEnd' not in val])
print("Students who study Python or Java: ", [key for key, val in students.items() if 'Java' in val or 'Python' in val])


# 3. Написать функцию перевода размеров женского белья из международного во все остальные. Внтри функции нужно просто
# обращаться к правильно составленному словарю.

sizes = {
    'XXS': {'Russia': 42, 'Germany': 36, 'USA': 8, 'France': 38, 'United Kingdom': 24},
    'XS': {'Russia': 44, 'Germany': 38, 'USA': 10, 'France': 40, 'United Kingdom': 26},
    'S': {'Russia': 46, 'Germany': 40, 'USA': 12, 'France': 42, 'United Kingdom': 28},
    'M': {'Russia': 48, 'Germany': 42, 'USA': 14, 'France': 44, 'United Kingdom': 30},
    'L': {'Russia': 50, 'Germany': 44, 'USA': 16, 'France': 46, 'United Kingdom': 32},
    'XL': {'Russia': 52, 'Germany': 46, 'USA': 18, 'France': 48, 'United Kingdom': 34},
    'XXL': {'Russia': 54, 'Germany': 48, 'USA': 20, 'France': 50, 'United Kingdom': 36},
    'XXXL': {'Russia': 56, 'Germany': 50, 'USA': 22, 'France': 52, 'United Kingdom': 28}}

size_int = input("Input international size: ")
to_size = input("Convert to size: ")


def convert(size):
    print("Receive your", to_size, "size: ", sizes[size_int][to_size])


convert(size_int)








