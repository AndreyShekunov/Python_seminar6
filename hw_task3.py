# Задача 3. Дан список. Выведите те его элементы, которые встречаются
#  в списке только один раз.
#  Элементы нужно выводить в том порядке, в котором они встречаются в списке.)

# Исходный вариант

# import random
# a = [random.randint(-10,10) for i in range(10)]
# print (a)
# lst = []
# for i in a:
#     if a.count(i)==1:
#         lst.append(i)
# print ()
# print (lst)

# Модифицированный вариант

import random
a = list(map(int, input().split()))
print(list(filter(lambda i: a.count(i) == 1, a)))
