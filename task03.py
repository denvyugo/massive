#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

limit = 10
size = 10
list = [random.randint(0,limit) for _ in range(size)]
print(list)
emax = list[0]
emin = list[0]
imax = 0
imin = 0
for i, item in enumerate(list):
    if item > emax:
        emax = item
        imax = i
    if item < emin:
        emin = item
        imin = i

list[imax], list[imin] = list[imin], list[imax]
print(list)