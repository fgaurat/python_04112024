

class Rectangle2:

    def __init__(self, longueur, largeur):
        assert longueur > 0 and largeur > 0
        
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        assert longueur > 0
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        assert largeur > 0
        self.__largeur = largeur

    def get_surface(self):
        return self.__largeur*self.__longueur

    
    def __str__(self):
        return f"Rectangle {self.__longueur=}, {self.__largeur=}"
    
    def __eq__(self,obj):
        return self.__longueur == obj.__longueur and self.__largeur == obj.__largeur
    
    
    longueur = property(get_longueur,set_longueur)
    largeur = property(get_largeur,set_largeur)