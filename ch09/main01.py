from Rectangle import Rectangle

def main():
    r = Rectangle(1,2)
    
    #region c'est mal
    # C'est mal
    # print(r._longueur)
    # print(r._largeur)
    # r._longueur = -1000
    # print(r._longueur)
    #  print(r._Rectangle__longueur)
    #endregion
    
    l = r.get_longueur()
    print(l) # 4
    r.set_longueur(12)
    
    l = r.get_longueur()
    print(l) # 12
    
    l = r.get_largeur()
    print(l) # 2
    r.set_largeur(7)
    l = r.get_largeur()
    print(l) # 7
    
    s = r.get_surface()
    assert s ==84
    
    print(50*'-')
    
    string_rectangle = str(r)
    print(string_rectangle)
    print(r)
    r = Rectangle(1,2)
    r1 = Rectangle(1,2)
    
    # if r.__eq__(r1):
    if r==r1:
        print("ok")
    else:
        print("ko")
    print(50*'-')
    
    r = Rectangle()
    r.longueur = 12
    r.longueur = -12
          
    print(r.longueur)
    
if __name__=='__main__':
    main()
