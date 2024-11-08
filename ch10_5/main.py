from timeit import timeit

def l1():
    l=[]
    for i in range(100):
        l.append(i)

def l2():
    l=list(map(lambda i:i,range(100)))

def l3():
    l=[i for i in range(100)]



def main():
    t1 = timeit(l1)
    t2 = timeit(l2)
    t3 = timeit(l3)
    print(t1)
    print(t2)
    print(t3)
    
if __name__=='__main__':
    main()