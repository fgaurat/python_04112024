from collections import deque
import os
os.system("cls")

l = [10, 20, 30, 40, 50]

l.append(60)
print(l)
last_value = l.pop()
print(last_value)
print(l)
l2 = [60, 70, 80]
l3 = l+l2
print(l3)

l.extend(l2)
print(l)
to_find = 30
if to_find in l:
    print("ok")

d = deque(l)
print(d)
d.appendleft(-10)
print(d)


print(50*'-')
l = []
for i in range(10, 60, 10):
    l.append(i)
print(l)

l = list(map(lambda i: i*10, range(1, 6)))
print(l)


l = [i for i in range(10, 60, 10)]
print(l)

lines = ['  ligne 01  ', 'ligne 02  ', '  ligne 03']
l = [line.strip() for line in lines]
print(lines)
print(l)

a = 1
del a
print(a)
