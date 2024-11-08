def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n=10):    # write Fibonacci series up to n
    """Return a Fibonacci series up to n."""
    l = []
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b
    return l

# Now call the function we just defined:
fib(10)
result = fib2(10)
# [0,1,1,2,3,5,8]
print(result) 

result = fib2()
print(result)

print(50*'-')


a = 12
def f(p=a):
    # global a
    # a= 258
    print("dans f",p)


# print("avant f",a)
a = 5698
f()
# print("après f",a)

print(50*'-')

def f2(a,l=[]):
    l.append(a)
    print(l)
    
f2(5)    # [5]
f2(8)    # [8] ou [5,8]
f2(815)    # [815] ou [5,8,815]
print(50*'-')


def hello(name,first_name):
    print("Bonjour nom:",name,"first_name:", first_name)
hello('GAURAT',"Frédéric")
hello(first_name="Frédéric",name='GAURAT') 