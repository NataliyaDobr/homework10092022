#print(sum([int(i) for i in input() if i.isdigit()]))
#1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# import time
# n = time.time_ns()
# print(n)
# print(str(n)[-3])

#2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# sp = []
# for _ in range(7):
#     sp.append(input())
#
# print(sp)
#
# n = int(input())
#
# flag = False
# for i in sp:
#     if str(n) in i:
#         flag = True
#         print('Число есть в элементе списка')
#         break
# if not flag:
#     print('Числа в списке не оказалось')

# решение второй задачи преподавателем:
# some_list = [input('Введите строку ') for _ in range(int(input('введите число ')))]
# el = input('Введите искомое число: ')
# if el in some_list:
#     print('yes')
# else:
#     print('no')

#3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# spisok = []
# for _ in range(4):
#     spisok.append(input())
# print(spisok)
# n = str(input())
# for i in spisok:
#     cnt = 1
#     if str(n) in i:
#         cnt+=1
#         if cnt==2:
#             print(spisok.index(i))
#             break
# else:
#     print('нет второго вхождения')

# решение третьей задачи преподавателем
some_list = [input('Введите строку ') for _ in range(int(input('введите число ')))]
el = input('Введите искомую строку: ')
c = 0
if some_list.count(el) < 2:
    print('-1')
else:
    for i in range(len(some_list)):
        if some_list[i] ==1:
            c += 1
        if c == 2:
            print(i)
            break

