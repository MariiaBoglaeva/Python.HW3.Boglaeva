# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

num_list = []
for _ in range(10):
    num_list.append(random.randint(1, 10))
print(num_list)
multiplication_list = []
if len(num_list) % 2 == 0:
    limit = int(len(num_list) / 2)
else:
    limit = int(len(num_list) / 2 + 1)
for i in range(limit):
    multiplication_num = num_list[i] * num_list[len(num_list) - 1 - i]
    multiplication_list.append(multiplication_num)
print(multiplication_list)
