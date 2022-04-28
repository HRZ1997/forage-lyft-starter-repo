from abc import ABC, abstractclassmethod

#interface
class Battery(ABC):

    @abstractclassmethod
    def battery_needs_service(self):
        pass