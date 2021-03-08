import pygame
from Entities.Ball import Ball
from Entities.Player import Player

class Game_Board:

    def __init__(self, tile_size, n_tiles_width, n_tiles_height, board_width_offset, board_height_offset):
        # Base initialization
        self.tile_size = tile_size
        self.map_width = n_tiles_width
        self.map_height = n_tiles_height
        self.board_height_offset = board_height_offset
        self.board_width_offset = board_width_offset
        
        # Initialize world
        self.world = self.create_map()
        self.entities = []

    def init_entities(self, entities):
        for key in entities.keys():
            if key == "players":
                for player in entities[key]:
                    column = player['x']
                    row = player['y']
                    pos = (self.world[row][column], player['width'], player['height'])

                    player = Player(*pos, 255, player['id'], self.tile_size)
                    self.entities.append(player)
            
            elif key == 'balls':
                for ball in entities[key]:
                    column = ball['x']
                    row = ball['y']
                    pos = (self.world[row][column], ball['width'], ball['height'])

                    ball = Ball(*pos, 100, self.tile_size)
                    self.entities.append(ball)

    def create_map(self):
        """
        Returns a list with lists of tuples which symbolize every tile
        on the board. 
        """
        map_pos_x = self.board_width_offset
        map_pos_y = self.board_height_offset 
        world = []
        
        for lines in range(0, self.map_height):
            line = []

            for tile in range(0, self.map_width):
                curr_tile = (int(tile * self.tile_size + map_pos_x),
                             int(lines * self.tile_size + map_pos_y))
                line.append(curr_tile)

            world.append(line)

        return world

    def update(self, world, entities):
        for entity in self.entities:
            upd_entity = None
            
            if type(entity) == Player:        
                upd_entity = list(filter(lambda x: entity.identification == x['id'], entities['players']))[0]

            elif type(entity) == Ball:
                # Denna kan vara såhär i dagsläget med endast en boll
                upd_entity = entities['balls'][0]
            
            entity.update(upd_entity, self.world)

    def render(self, screen, font, entities=[]):
        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, 0, (self.board_width_offset, self.board_height_offset,
                                     self.tile_size*self.map_width, self.tile_size*self.map_height), 1)

        self.draw_entities(screen)
        
        pygame.display.update()
        pygame.display.flip()

    def draw_entities(self, screen):
        for entity in self.entities:
            print(entity.get_entity_drawing_props())
            pygame.draw.rect(screen, entity.color, 
                            entity.get_entity_drawing_props())
