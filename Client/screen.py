import requests
import pygame
import pygame.locals
from uuid import uuid4
from game_state import Game_State
from Board import Game_Board

class Screen():
    def __init__(self):
        self.identity = self.create_unique_id()
        self.screen_width = 1200
        self.screen_height = 960
        self.world_position = ()
        
        # Gameboard
        self.game_board = Game_Board(tile_size = 10, 
                                     n_tiles_width=25,
                                     n_tiles_height=25,
                                     board_width_offset = self.screen_width / 5,
                                     board_height_offset = self.screen_height / 4)
        
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
            self.render(screen, font)#, self.screen_height, self.screen_width)
            
            pressed_key = "Not pressed"
            
            # Check when a game is to be started
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
                        outcome = game.start(screen, font) 

                    if len(outcome) == 0:
                        shut_down = True

                clock.tick(5)

        return outcome
                    
    def render(self, screen, font, state=None):#, sw, sh):
        screen.fill((255,255,255))

        if state == None:
            screen.blit(self.text(font, "Press enter to start the game!"), (self.screen_width / 2.5, (self.screen_height) / 4))
        
        else:            
            # Låt board hantera sin egen render då den kommer hålla world
            self.game_board.render(screen, font)
        
        
        pygame.display.update()
        pygame.display.flip()
        
    def text(self, font, text, color = (0,0,0)):
        return font.render(text, False, color)



if __name__ == '__main__':
    client = Screen()
    client.start()