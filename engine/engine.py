from abc import ABC, abstractmethod

#interface
class Engine(ABC):

    @abstractmethod
    def engine_needs_service(self):
        pass