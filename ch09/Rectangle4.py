

class Rectangle4:
    __cpt=0
    def __init__(self, longueur, largeur):
        assert longueur > 0 and largeur > 0
        
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle4.__cpt+=1

    @classmethod
    def build_from_csv(cls,value):
        values = [int(v) for v in value.split(';')]
        r = cls(*values)
        return r
    
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

    @staticmethod
    def get_cpt():
        return Rectangle4.__cpt

    def get_surface(self):
        return self.__largeur*self.__longueur

    def __str__(self):
        return f"Rectangle {self.__longueur=}, {self.__largeur=}"
    
    def __eq__(self,obj):
        return self.__longueur == obj.__longueur and self.__largeur == obj.__largeur
    
