from Entities.Moving_Entity import Entity

class Ball(Entity):

    def __init__(self, position, tiles_width, tiles_height, color):
        self.position_x = position[0]
        self.position_y = position[1]
        self.width      = tiles_width
        self.height     = tiles_height
        self.color      = color
        # speed, x, y
        self.direction  = [1, 0, 0]
