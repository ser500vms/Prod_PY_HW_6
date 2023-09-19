# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного
# минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]

# Вариант 1:

# list = [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]

# max, min = 10, 7

# for i in range(len(list)):
#     if min <= list[i] <= max:
#         print(i, end=' ')

# Вариант 2:

list = [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]

max, min = int(input('введите максимальную границу диапазона: ')), \
int(input('введите минимальную границу диапазона: '))

new_list = [i for i in range(len(list)) if min <= list[i] <= max]
print(new_list)