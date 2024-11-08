from Rectangle import Rectangle


class Carre(Rectangle):
    """ C'est la class Carre"""
    def __init__(self, cote):
        """ Init"""
        super().__init__(cote, cote)
        self.__cote = cote

    @property
    def cote(self):
        return self.__cote

    @cote.setter
    def cote(self, cote):
        self.__cote = cote
        self.longueur = cote
        self.largeur = cote

    def __str__(self):
        return f"{__class__.__name__} {self.__cote=}"
