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
some_list = [int(input('Введите строку ')) for _ in range(int(input('введите число ')))]
print(some_list)
new_list = some_list[::-1]
print(new_list)
for i in range(round(len(some_list)/2)):
    result = some_list[i]*new_list[i]
    print(result)