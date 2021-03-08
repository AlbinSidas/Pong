from abc import ABC, abstractmethod

class Entity(ABC):

    @abstractmethod
    def __init__(self, positon, tiles_width, tiles_height, color, tile_size):
        raise NotImplementedError()        
        
    @abstractmethod
    def update(self, entity, world):
        """
        update is not a derived funciton as
        different updateds with powerups can be used
        on different moving entities (player can maybe gain something
        the ball cant etc.)
        """
        raise NotImplementedError()        
    
    def get_entity_drawing_props(self):
        return (self.x, self.y, self.width, self.height)
