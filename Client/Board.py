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
        
        # Initialize default enteties
        self.entities = []
        self.init_entities()

    def init_entities(self):
        # Find initial values for middle of the board.
        height_middle = len(self.world) // 2
        width_middle = len(self.world[0]) // 2

        # Set global player plattform settings
        player_width = 1
        player_height = 4

        ball_widht = 1
        ball_height = 1
        
        # p1 will be on the left side starting in middle
        p1_pos = [self.world[height_middle - (player_height//2)][1], player_width*self.tile_size, player_height*self.tile_size]
        player1 = Player(*p1_pos, 255, True)
        
        # p2 will be on the right side starting in the middle
        p2_pos = [(self.world[height_middle - player_height//2][-2]), player_width*self.tile_size, player_height*self.tile_size]
        player2 = Player(*p2_pos, 255, False)

        # Ball is spawned in the middle
        ball_pos = (self.world[height_middle - ball_height][width_middle - 1], ball_widht*self.tile_size, ball_height*self.tile_size)
        ball     = Ball(*ball_pos, 255)

        self.entities.append(player1)
        self.entities.append(player2)
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

    def render(self, screen, font, entities=[]):
        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, 0, (self.board_width_offset, self.board_height_offset,
                                     self.tile_size*self.map_width, self.tile_size*self.map_height), 1)

        self.drawer(screen)
        
        pygame.display.update()
        pygame.display.flip()

    def drawer(self, screen):
        
        """
        for lines in self.world:
            for tile in lines:
                pygame.draw.rect(screen, 0,(tile[0], tile[1],
                                            self.tile_size, self.tile_size),1)

        """
        for entity in self.entities:
            print(entity.color)
            print(entity.get_entity_drawing_props())
            pygame.draw.rect(screen, entity.color, 
                            entity.get_entity_drawing_props())
