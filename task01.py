# Найти количество различных подстрок в строке
import hashlib


somestr = input('введите какую-то строку: ')
hashdict = {}

for i in range(len(somestr)):
    for j in range(i + 1, len(somestr)+1):
        substr = somestr[i:j]
        subhash = hashlib.sha1(substr.encode('utf-8')).hexdigest()
        print(subhash)
        if subhash not in hashdict:
            hashdict[subhash] = substr

print(len(hashdict))

