import traceback

class DivBy12Error(Exception):
    
    
    def __init__(self):
        super().__init__('Division par 12')


def div(a,b):
    if b == 12:
        raise DivBy12Error()
    return a/b

def call_div(a,b):
    r=0
    try:
        print("OPEN LOG")
        r = div(a,b)
    finally:
        print("CLOSE LOG")
    return r

def main():
    try:
        a = 3
        # b = int(input('b: '))
        b = 12
        c = call_div(a,b)
        print('result',c)
    except DivBy12Error as e:
        print("mon erreur",e)
    except ZeroDivisionError as e:
        print("erreur",e)
        # stack_trace = traceback.extract_tb(e.__traceback__)
        # print(stack_trace[-1])
        # # traceback.print_exc()
    except TypeError as e:
        print("erreur",e)
    except ValueError as e:
        print("erreur",e)        
    except Exception as e:
        print("erreur",e)        
    else:
        print("pas d'erreur")
    finally:
        print("finally")
    print("La suite")
        
if __name__=='__main__':
    main()
