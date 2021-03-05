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

    def init_entities(self, entities, client_identification):
        for key in entities.keys():
            if key == "players":
                for player in entities[key]:

                    column = player['x']
                    row = player['y']
                    pos = (self.world[row][column], player['width'] * self.tile_size, player['height'] * self.tile_size)

                    player = Player(*pos, 255, player['id'] == client_identification)
                    self.entities.append(player)


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

    def render(self, screen, font, entities=[]):
        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, 0, (self.board_width_offset, self.board_height_offset,
                                     self.tile_size*self.map_width, self.tile_size*self.map_height), 1)

        self.drawer(screen)
        
        pygame.display.update()
        pygame.display.flip()

    def drawer(self, screen):
        print("INNE I DRAWER", self.entities)
        """
        for lines in self.world:
            for tile in lines:
                pygame.draw.rect(screen, 0,(tile[0], tile[1],
                                            self.tile_size, self.tile_size),1)

        """
        for entity in self.entities:
            print(entity)
            pygame.draw.rect(screen, entity.color, 
                            entity.get_entity_drawing_props())
