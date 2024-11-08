def add(*l): # par position en nombre variable
    print(l)
    t=0
    for v in l:
        t = t+v
    
    return t

values = [1,2,3,4,5]
r = add(*values)
# r = add(1,2,3,4,5)
print(r) # 15


print(*values)


a,b,*c = [15,26,15,58]
print(a,b,c)

l = [58,78,98]
a,b,c = [*l]
print(a,b,c)

print(50*'-')


def hello(**d):
    print(d)
    print("Bonjour nom:",d['name'],"first_name:", d['first_name'])

hello(first_name="Frédéric",name='GAURAT',job="dev",age="48") 