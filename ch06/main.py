import sys
# sys.path.append("./malib")
# import fibo as fb
# from fibo import fib as remote_fib
from fibo import *
# fibo.fib(1000)
# fb.fib(1000)
# import thelib.hello
from thelib.hello import say_hello

from fibo import fib 

def fib(i):
    print("Bonjour fib")


def main():
    print(sys.argv)
    # value = int(sys.argv[-1])
    value = 1000
    fib(value)
    print(sys.path)
    say_hello("freds")

if __name__=='__main__':
    main()
