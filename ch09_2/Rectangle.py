from ICalcGeo import ICalcGeo


class Rectangle(ICalcGeo):

    def __init__(self, longueur, largeur):
        assert longueur > 0 and largeur > 0
        
        self.__longueur = longueur
        self.__largeur = largeur

    @property
    def longueur(self):
        return self.__longueur
    
    @longueur.setter
    def longueur(self, longueur):
        assert longueur > 0
        self.__longueur = longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self, largeur):
        assert largeur > 0
        self.__largeur = largeur

    def get_surface(self):
        return self.__largeur*self.__longueur

    def __str__(self):
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"
    
    def __eq__(self,obj):
        return self.__longueur == obj.__longueur and self.__largeur == obj.__largeur
    
