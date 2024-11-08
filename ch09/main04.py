from Rectangle4 import Rectangle4
def main():
    r = Rectangle4(6,4)
    r2 = Rectangle4(62,44)
    print(r.longueur)
    r.longueur = 25
    print(r)
    
    # C'est mal
    print(r.get_cpt())
    print(r2.get_cpt())
    print(Rectangle4.get_cpt())
    r3 = Rectangle4.build_from_csv('4;2')
    print(r3)    
    print(Rectangle4.get_cpt())
if __name__=='__main__':
    main()




def toto(n):
    return n