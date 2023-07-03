# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

diap = [i for i in range(int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: ')) + 1)]
print(spisok := [random.randint(0, 30) for _ in range(20)])
print([i for i in range(0, len(spisok)) if spisok[i] in diap])
