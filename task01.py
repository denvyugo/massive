# Найти количество различных подстрок в строке
import hashlib


somestr = input('введите какую-то строку: ')
hashdict = {}

for i in range(len(somestr)):
    for j in range(i + 1, len(somestr)+1):
        print(i, j,)
        print(somestr[i:j])
        substr = somestr[i:j]
        subhash = hashlib.sha1(substr.encode('utf-8')).hexdigest()
        print(subhash)
        if not in hashdict[subhash]:
            hashdict[subhash] = substr

