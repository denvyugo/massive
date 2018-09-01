# Определить, какое число в массиве встречается чаще всего.
import random
import cProfile


MIN_NUMBER = -1000
MAX_NUMBER = 1000
LIST_SIZE = 100000

def mk_list(min_n, max_n, size):
    list = [random.randint(min_n, max_n) for _ in range(size)]
    print(list)
    return list

def num_freq(lst):
    max_freq = 0
    max_freq_n = 0
    for j in range(len(lst)):
        numb = lst[j]
        freq = 0
        for i in lst:
            if i == numb:
                freq += 1
        if freq > max_freq:
            max_freq_n = numb
            max_freq = freq
    print(max_freq, max_freq_n)

def get_num_freq_cycle():
    nbs = mk_list(MIN_NUMBER, MAX_NUMBER, LIST_SIZE)
    num_freq(nbs)

# python -m timeit -n 100 -s "import task04" "task04.get_num_freq_cycle"
# 100 loops, best of 5: 46.6 nsec per loop
# cProfile.run('get_num_freq_cycle()')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.045    0.045    0.045    0.045 task04.py:15(num_freq)
# 1    0.000    0.000    0.052    0.052 task04.py:29(get_num_freq_cycle)
# LIMIT_SIZE = 100000
# 1  439.276  439.276  439.276  439.276 task04.py:15(num_freq)
# 1    0.000    0.000  439.612  439.612 task04.py:29(get_num_freq_cycle)

def num_freq_d(list):
    freq_dict = {}
    for i in list:
        if i not in freq_dict:
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1
    max_freq = 0
    max_freq_n = 0
    for key, freq in freq_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_freq_n = key
    print(max_freq, max_freq_n)

def get_num_freq_dict():
    nbs = mk_list(MIN_NUMBER, MAX_NUMBER, LIST_SIZE)
    num_freq_d(nbs)

# python -m timeit -n 100 -s "import task04" "task04.get_num_freq_dict"
# 100 loops, best of 5: 46.6 nsec per loop
# cProfile.run('get_num_freq_dict()')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.000    0.000 task04.py:40(num_freq_d)
# 1    0.000    0.000    0.003    0.003 task04.py:55(get_num_freq_dict)
# LIST_SIZE = 100000
# 1    0.021    0.021    0.021    0.021 task04.py:43(num_freq_d)
# 1    0.000    0.000    0.298    0.298 task04.py:58(get_num_freq_dict)

def num_freq_p(list):
    num_set = set(list)
    max_freq = 0
    max_freq_n = 0
    for i in num_set:
        freq = list.count(i)
        if freq > max_freq:
            max_freq = freq
            max_freq_n = i
    print(max_freq, max_freq_n)

def get_num_freq_python():
    nbs = mk_list(MIN_NUMBER, MAX_NUMBER, LIST_SIZE)
    num_freq_p(nbs)

# python -m timeit -n 100 -s "import task04" "task04.get_num_freq_python"
# 100 loops, best of 5: 46.6 nsec per loop
# cProfile.run('get_num_freq_python()')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.006    0.006 task04.py:66(num_freq_p)
# 1    0.000    0.000    0.016    0.016 task04.py:77(get_num_freq_python)
# LIST_SIZE = 100000
# 1    0.009    0.009    5.605    5.605 task04.py:72(num_freq_p)
# 1    0.000    0.000    5.868    5.868 task04.py:83(get_num_freq_python)

# if __name__ == '__main__':
#     nbs = mk_list(MIN_NUMBER, MAX_NUMBER, LIST_SIZE)
#     num_freq(nbs)
#     num_freq_d(nbs)
#     num_freq_p(nbs)

