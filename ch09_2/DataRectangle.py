from dataclasses import dataclass

@dataclass
class DataRectangle:
    largeur:int=0
    longueur:int=0
    
    
    def get_surface(self):
        return self.longueur * self.largeur