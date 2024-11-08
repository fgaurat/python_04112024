t = (12,15,89)
print(t)

# TypeError: 'tuple' object does not support item assignment
# t[0] = 159

l = [11,"toto",1.5]
t = 12,15,89
print(t)
a,b = 0,1


def f():
    v1 = 12
    v2 = 89
    return v1,v2

a,b = f()