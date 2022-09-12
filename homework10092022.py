# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# some_list = [int(input('Введите строку '))for _ in range(int(input('введите число ')))]
# print(some_list)
# new_list = some_list[1::2]
# print(new_list)
# sum_el = sum(new_list)
# print(sum_el)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# some_list = [int(input('Введите строку ')) for _ in range(int(input('введите число ')))]
# print(some_list)
# new_list = some_list[::-1]
# print(new_list)
# for i in range(round(len(some_list)/2)):
#     result = some_list[i]*new_list[i]
#     print(result)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# fract_part = []
# some_list = [float(input('Введите числа ')) for _ in range(int(input('введите число ')))]
# print(some_list)
# for i in range(len(some_list)):
#     fract_part.append(some_list[i]-int(some_list[i]))
# print(fract_part)
# print(max(fract_part)-min(fract_part))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# new_digit=[]
# digit = int(input('Введите число '))
# while digit > 1:
#     rem = digit%2
#     #print(rem)
#     new_digit.append(rem)
#     digit = digit//2
# new_digit.append(digit)
# print(" ".join(map(str, new_digit[::-1])))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('Введите число '))
m=n
fib = [0,1]
while len(fib) < n+1:
    fib.append(fib[-2]+fib[-1])
print(fib)
neg_fib = [1,-1]
while len(neg_fib) < m:
    neg_fib.append(neg_fib[-2]-neg_fib[-1])
print(neg_fib)
print(" ".join(map(str, neg_fib[::-1]))," ".join(map(str, fib)))




