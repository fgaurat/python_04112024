import typing

def oldmult2(l:list)->list:
    t = []
    for value in l:
        t.append(value*2)
    return t


def mult2(value):
    return value*2


values = [1,2,3,4,5]
# new_values = mult2(values)
# new_values = list(map(mult2,values))
new_values = list(map(lambda v:v*2 ,values))

print(new_values) #  [2,4,6,8,10]

l =oldmult2(new_values)