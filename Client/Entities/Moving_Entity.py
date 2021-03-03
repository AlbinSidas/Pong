from abc import ABC, abstractmethod

class Entity(ABC):

    @abstractmethod
    def __init__(self, positon, tiles_width, tiles_height, color):
        raise NotImplementedError()        
        
    def get_entity_drawing_props(self):
        return (self.position_x, self.position_y, self.width, self.height)
