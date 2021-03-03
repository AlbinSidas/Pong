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
        max_right = self.world[0][-1]
        max_left  = self.world[0][0]
        height_middle = len(self.world) // 2
        width_middle = len(self.world[0]) // 2

        # Set global player plattform settings
        player_width = 1
        player_height = 4

        ball_widht = 1
        ball_height = 1
        
        # p1 will be on the left side starting in middle
        p1_pos = (max_left, height_middle - player_height//2, player_width, player_height)
        player1 = Player(*p1_pos, 200, True)
        
        # p2 will be on the right side starting in the middle
        p2_pos = (max_right, height_middle - player_height//2, player_width, player_height)
        player2 = Player(*p2_pos, 100, False)

        # Ball is spawned in the middle
        ball_pos = (width_middle, height_middle - ball_height, ball_widht, ball_height)
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
        """
        Handles all the positioning and updating for each frame. 
        """
        #world_side_length = self.tile_size * len(self.world)
        #frame_pos_x = self.world[0][0][0]
        #frame_pos_y = self.world[0][0][1]
        #score_text = font.render("Your score: {}".format(snake.score),
        #                         False, (0,0,0))

        screen.fill((255, 255, 255))
        #screen.blit(score_text, (self.screen_width / 4 , self.screen_height / 1.7))

        pygame.draw.rect(screen, 0, (self.board_width_offset, self.board_height_offset,
                                     self.tile_size*self.map_width, self.tile_size*self.map_height), 1)
        """
        pygame.draw.rect(screen, 0, (frame_pos_x, frame_pos_y,
                                     world_side_length, world_side_length), 1)
        """

        
        self.drawer(screen, entities)#, snake, fruit_list)
        
        pygame.display.update()
        pygame.display.flip()

    def drawer(self, screen, entities):
        
        """
        Kolla på om jag kan göra objekt av entities, 
        iterera över entities, ta ut deras tiles/positioner
        och sedan endast måla dessa, känns dum att behöva 
        iterera över hela världen
        """

        for entity in self.entities:
            pygame.draw.rect(screen, entity.color, 
                            entity.get_entity_drawing_props())


        for lines in self.world:
            for tile in lines:
                print(tile)
                pygame.draw.rect(screen, 0,(tile[0], tile[1],
                                            self.tile_size, self.tile_size), 1)
                """
                for body in snake.body:

                    if tuple(body) == tiles:
                        #Checks where the head of the snake is on the board.
                        pygame.draw.rect(screen, 0,(body[0], body[1],
                                                    self.tile_size, self.tile_size))
                
                
                if fruit_list[0].pos == tiles:
                    pygame.draw.rect(screen, 155,
                                    (tiles[0], tiles[1], self.tile_size, self.tile_size))
                #Draws every rectangle in the playingfield
                #pygame.draw.rect(screen, 0,(tiles[0], tiles[1],
                #                          tile_width, tile_height), 1)
                    
                """
                
         



