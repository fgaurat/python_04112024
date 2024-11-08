from Carre import Carre
from Cercle import Cercle
from DataRectangle import DataRectangle

def main():
    c = Carre(5)
    print(c)
    print(c.cote)
    print(c.get_surface())
    c.cote=2
    print(c.get_surface())
    print(50*'-')
    ce = Cercle(5)
    print(ce.get_surface())
    d = DataRectangle(12,4)
    d1 = DataRectangle(12,4)
    print(d)
    if d==d1:
        print('ok')
    d.longueur = 89
    print(d)
    print(d.get_surface())
    
if __name__=='__main__':
    main()
