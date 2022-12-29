# Задача 2. Задайте список из n чисел последовательности (1+1/n)^n

# Исходный вариант
n = int(input('Введите число N = '))
lst = []
for i in range(1, n+1):
    lst.append((1+1/i)**i)
print(lst)

# Модифицированный вариант
lst = [i for i in range(1, int(input('Введите число N = '))+1)]
print(list(map(lambda i: (1+1/i)**i, lst)))
