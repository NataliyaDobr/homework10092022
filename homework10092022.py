# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
some_list = [int(input('Введите строку '))for _ in range(int(input('введите число ')))]
print(some_list)
new_list = some_list[1::2]
print(new_list)
sum_el = sum(new_list)
print(sum_el)