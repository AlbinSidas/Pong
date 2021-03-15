from Entities.Moving_Entity import Entity

class Player(Entity):

    def __init__(self, position, tiles_width, tiles_height, color, identification, tile_size):
        self.x          = position[0]
        self.y          = position[1]
        self.color      = color
        self.identification = identification
        self.tile_size = tile_size
        self.width      = tiles_width * self.tile_size
        self.height     = tiles_height * self.tile_size
        
    def update(self, updated, world):
        self.x = world[updated['y']][updated['x']][0]
        self.y = world[updated['y']][updated['x']][1]
        self.width = updated['width'] * self.tile_size
        self.height = updated['height'] * self.tile_size



    