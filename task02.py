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
somestr = 'beep boop beer!'
cntr = Counter(somestr)
qchar =deque()
ordc = OrderedDict(sorted(cntr.items(), key=lambda t: t[1]))
print(ordc)
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

curn = n # current node
pren = None # previous node
stack = [] # stack on browsing nodes
codes = {} # dictionary for codes
# moving on tree
# directions
DN = 1
UP = 0
LF = 0
RT = 1
dep = DN # moving on depth
wid = LF # moving on width
path = ''
while True:
    # print(curn)
    if curn is n and dep == UP and wid == RT:
        break
    if dep == DN and wid == LF:
        if curn.left is not None:
            stack.append(curn)
            curn = curn.left
            path = ''.join((path, str(wid)))
        else:
            # check on a leaf on a right
            dep = DN
            wid = RT
    if dep == DN and wid == RT:
        if curn.right is not None:
            stack.append(curn)
            curn = curn.right
            path = ''.join((path, str(wid)))
            wid = LF
        else:
            # leaf on right - save in dict of codes
            codes[curn.data] = path
            dep = UP
    if dep == UP:
        if len(stack) != 0:
            pren = stack.pop()
            if pren.left is curn:
                dep = DN
                wid = RT
            curn = pren
            path = path[:-1]

print(codes)

# print coding string
for x in somestr:
    stack.append(codes[x])

print(''.join(stack))

