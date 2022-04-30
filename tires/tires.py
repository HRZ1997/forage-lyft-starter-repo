from abc import ABC, abstractclassmethod

#interface
class Tires(ABC):

    @abstractclassmethod
    def tires_need_service(self):
        pass
