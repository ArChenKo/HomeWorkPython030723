# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a, n, d = int(input('Введите первое число: ')), int(input('Введите размер списка: ')), int(input('Введите шаг '
                                                                                                 'прогрессии: '))
print([i for i in range(a, a + (n - 1) * d + 1, d)])
