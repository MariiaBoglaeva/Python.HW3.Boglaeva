# Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
def fibbonacci(n):
    if n >= 0:
        if n == 1:
            return 1
        elif n ==0:
            return 0
        else:
            return fibbonacci(n - 1) + fibbonacci(n - 2)
    elif n < 0:
        if n == -1:
            return 1
        else:
            return fibbonacci(n + 2) - fibbonacci(n + 1)


num = int(input("Введите число: "))
fibb_list = []
for i in range(-num, num + 1):
    fibb_list.append(fibbonacci(i))
print(fibb_list)
