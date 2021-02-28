import requests
import pygame
import pygame.locals
from uuid import uuid4
from game_state import Game_State

class Screen():

    def __init__(self):
        """
        Hantera input?
        Lägga till vad man ska connecta mot på commandline?
        """

        self.identity = self.create_unique_id()
        self.screen_width = 1200
        self.screen_height = 960
        
    def create_unique_id(self):
        return str(uuid4())

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        font = pygame.font.get_default_font()
        font = pygame.font.SysFont(font, 24)
        clock = pygame.time.Clock()
        
        # Checks if user wants to close the game. 
        shut_down = False

        # This will mark the current choosen menu alternative.
        choice = 0

        # This will hold information about which keys has been pressed this loop.
        key_list = []

        # Outcome-list will hold information about the game,
        # if exited or if it should add new scores to highscore etc.
        outcome = []

        # Converts a keystroke value (up, down, right, left) to values to
        # add to choice.
        key_converter = {
            "273" : -1,
            "274" : 1,
            "275" : 1,
            "276" : -1
        }


        while not shut_down:
            self.render(screen, font, choice)#, self.screen_height, self.screen_width)
            
            pressed_key = "Not pressed"
            
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    shut_down = True
                elif event.type == pygame.locals.KEYDOWN:
                    # Converted because this is the key in the converter.
                    pressed_key = str(event.key)

            if pressed_key != "Not pressed": 
                key_list.append(pressed_key)
            
            if len(key_list) != 0:
                key = key_list.pop()

                """
                if key in key_converter:
                    
                    choice += key_converter[key]
                    if choice > 2:
                        choice = 0
                    elif choice < 0:
                        choice = 2
                """

                # Enterkey
                if key == "13":
                    # TODO
                    """
                    Kommer endast att vara ett start alternativ. 
                    Bör redan ha fått information om start states från 
                    servern här, alltså bör en request skicaks typ direkt för att spela 
                    där id etc är skickat till backenden. 
                    """
                    if choice == 0:
                        
                        game = Game_State(self)
                        outcome = game.start()
                        #outcome = start_game.start(screen, font)
                   
                    elif choice == 2:
                        shut_down = True

                    if len(outcome) > 0:
                        length = len(outcome)
                        if outcome[length - 1] == 0:
                            # Outcome is only returned if the player wants to exit. 
                            shut_down = True
                            
                        elif outcome[length - 3] == 10:
                            # Here I check the returnvalues if the screensize
                            # was changed in the config object.
                            self.screen_height = int(outcome[length - 2])
                            self.screen_width = int(outcome[length - 1])                    
                        
                clock.tick(5)
                    
    def render(self, screen, font, choice):#, sw, sh):
        """
        menu_title = self.text(font, "Menu")
        start = self.text(font, "Start")
        settings = self.text(font, "Settings")
        quiit = self.text(font, "Quit")
        sh = self.screen_height
        sw = self.screen_width
        """
        """
        if choice == 0:
            start = self.text(font, "Start", (220,20,60))
        elif choice == 1:
            settings = self.text(font, "Settings", (220, 20, 60))
        elif choice == 2:
            quiit = self.text(font, "Quit", (220 , 20, 60))
        """

        screen.fill((255,255,255))

        screen.blit(self.text(font, "Press enter to start the game!"), (self.screen_width / 2.5, (self.screen_height) / 4))
        
        """
        screen.blit(start, (sw/2, sh / 3))
        screen.blit(settings, (sw/2 - sw/40, sh / 2))
        screen.blit(quiit, (sw/2 , sh / 1.5))
        """

        pygame.display.update()
        pygame.display.flip()
        
    def text(self, font, text, color = (0,0,0)):
        return font.render(text, False, color)




class World:

    def __init__(self, config):
        self.tile_size = 0.01
        
        """
        """
        screen_width, screen_height = config.settings["Screensize"].split("x")
        self.screen_width = int(screen_width)
        self.screen_height = int(screen_height)

        self.tile_size = int(config.settings["Tilesize"])
        self.refreshrate = int(config.settings["Snake speed"])
        self.map_size = int(config.settings["Boardsize"])

        self.world = self.create_map()
        
    def create_map(self):
        """
        Returns a list with lists of tuples which symbolize every tile
        on the board. 
        """
        map_pos_x = self.screen_width / 4
        map_pos_y = self.screen_height / 8
        world = []
        
        for lines in range(0, self.map_size):
            line = []

            for tiles in range(0, self.map_size):
                tile = (int(tiles * self.tile_size + map_pos_x),
                        int(lines * self.tile_size + map_pos_y))
                line.append(tile)

            world.append(line)

        return world

    def render(self, screen, world, snake, fruit_list, font):
        """
        Handles all the positioning and updating for each frame. 
        """
        world_side_length = self.tile_size * len(self.world)
        frame_pos_x = self.world[0][0][0]
        frame_pos_y = self.world[0][0][1]
        score_text = font.render("Your score: {}".format(snake.score),
                                 False, (0,0,0))

        screen.fill((255, 255, 255))
        screen.blit(score_text, (self.screen_width / 4 , self.screen_height / 1.7))

        pygame.draw.rect(screen, 0, (frame_pos_x, frame_pos_y,
                                     world_side_length, world_side_length), 1)

        
        self.drawer(screen, world, snake, fruit_list)
        
        pygame.display.update()
        pygame.display.flip()

    def drawer(self, screen, world, snake, fruit_list):
        """
        Handles all drawing within the world rectangle. 
        """

        for lines in world:
            for tiles in lines:
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
                    
        
         



if __name__ == '__main__':
    client = Screen()
    client.start()