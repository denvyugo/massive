# Во втором массиве сохранить индексы четных элементов первого массива
import random

limit = 10
size = 10
list = [random.randint(0,limit) for _ in range(size)]
idx = []
for i, item in enumerate(list):
    if item % 2 == 0:
        idx.append(i)

print(list)
print(idx)
