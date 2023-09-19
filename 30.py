# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

fist_element, difference, amount_of_elements =  int(input('Введите первый элемент: ')), \
int(input('Введите разность: ')), int(input('Введите количество элементов: '))


arithmetic_progression_array = []
for i in range(amount_of_elements):
    arithmetic_progression_array.append(fist_element + i * difference)

print(arithmetic_progression_array)
