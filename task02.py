# Закодировать строку по алгоритму Хаффмана (сжатие)
from collections import Counter
from collections import deque
from collections import OrderedDict

class Node:

    def __init__(self, data=None, weit=None, left=None, right=None):
        self.data = data
        self.weit = weit
        self.left = left
        self.right = right

    def __repr__ (self):
        return f'node: {self.data}: {self.weit}'

# somestr = input('введите какую-нибудь строку: ')
somestr = 'bear beer beep'
cntr = Counter(somestr)
qchar =deque()
ordc = OrderedDict(sorted(cntr.items(), key=lambda t: t[1]))

for key, val in ordc.items():
    n = Node(key, val)
    qchar.append(n)

# построение дерева
while True:
    # создать новый узел, присоединить первых два
    n = Node()
    n.left = qchar.popleft()
    n.right = qchar.popleft()
    n.weit = n.left.weit + n.right.weit
    if len(qchar) == 0:
        break

    # ввернуть новый узел в очередь
    i = 0
    while n.weit > qchar[i].weit:
        i += 1
        if i == len(qchar):
            break
    if i > 0:
        qchar.rotate(-1 * i)
    qchar.appendleft(n)
    if i > 0:
        qchar.rotate(i)

# обход дерева
print(n)

