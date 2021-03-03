from Entities.Moving_Entity import Entity

class Player(Entity):

    def __init__(self, position, tiles_width, tiles_height, color, local_player):
        self.position_x = position[0]
        self.position_y = position[1]
        self.width      = tiles_width
        self.height     = tiles_height
        self.color      = color
        self.local_player = local_player
        
    