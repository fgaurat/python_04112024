from abc import ABC,abstractmethod

# class ICalcGeo:
    
#     def get_surface(self):
#         raise NotImplementedError('Hooooooo !')

class ICalcGeo(ABC):
    @abstractmethod
    def get_surface(self):
        pass