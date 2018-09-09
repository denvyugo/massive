# Во втором массиве сохранить индексы четных элементов первого массива
import random
import sys

limit = 10
size = 10
list = [random.randint(0,limit) for _ in range(size)]
idx = []
for i, item in enumerate(list):
    if item % 2 == 0:
        idx.append(i)

print(list, f'размер массива {sys.getsizeof(list)}')
print(idx, f'размер массива {sys.getsizeof(idx)}')
print(f'размеры всех переменных '
      f'{sys.getsizeof(list) + sys.getsizeof(idx) + sys.getsizeof(limit) + sys.getsizeof(size) + sys.getsizeof(i)}')