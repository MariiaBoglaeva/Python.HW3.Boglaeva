# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
num_decimal = int(input("Введите десятичное число: "))
num = num_decimal
i = 1
num_binary = 0
while num_decimal != 0:
    num_binary = num_binary + int(num_decimal % 2 * i)
    num_decimal = int(num_decimal / 2)
    i *= 10
print(f"{num}->{num_binary}")
