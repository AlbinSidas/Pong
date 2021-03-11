import requests
import json
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


    def create_unique_id(self):
        return str(uuid4())

    def init_game(self, init_settings):
        tile_size = init_settings['tileSize']
        width = init_settings['boardWidth']
        height = init_settings['boardHeight']

        # Get init settings from the server and initialize the gameboard
        # after that.
        self.game_board = Game_Board(tile_size = tile_size, 
                                     n_tiles_width=width,
                                     n_tiles_height=height,
                                     board_width_offset = self.screen_width / 5,
                                     board_height_offset = self.screen_height / 4)
        
        entities = init_settings['entities']
        self.game_board.init_entities(entities)
        
    def start(self):        
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        font = pygame.font.get_default_font()
        font = pygame.font.SysFont(font, 24)
        clock = pygame.time.Clock()
        
        # Checks if user wants to close the game. 
        shut_down = False

        # This will hold information about which keys has been pressed this loop.
        key_list = []

        # Outcome-list will hold information about the game,
        # if exited or if it should add new scores to highscore etc.
        outcome = []

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

                url = "http://localhost:3000"
                    
                # Enterkey
                if key == "13":
                        
                    r = requests.get(url + f"/initialize?id={self.identity}")
                    init_settings = json.loads(r.text)
                    
                    if not init_settings['success']:
                        print("Already too many players in the game, restart the nodeserver.")
                        exit()

                    self.game_board = None
                    self.init_game(init_settings)

                    game = Game_State(self)
                    outcome = game.start(screen, font) 

                    if len(outcome) == 0:
                        shut_down = True
                
                if key == "114":
                    r = requests.get(url + f"/reset")

                clock.tick(5)

        return outcome
                    
    def render(self, screen, font, in_game=False):#, sw, sh):
        screen.fill((255,255,255))

        if not in_game:
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