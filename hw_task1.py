# Задача 1. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# исходный вариант

import math

n = int(input('Введите число N = '))
lst = []
for i in range(1, n+1):
    lst.append(math.factorial(i))
print(lst)

# модернизированный вариант

print(list(math.factorial(i)
      for i in range(1, int(input('Введите число N = '))+1)))
