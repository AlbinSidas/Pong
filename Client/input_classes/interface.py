from abc import ABC, abstractmethod

class Interface(ABC):
    
    @abstractmethod
    def get_action(self, world):
        """
        This must be implemented in all subclasses
        """
        raise NotImplementedError()