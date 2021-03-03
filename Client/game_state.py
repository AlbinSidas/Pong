import pygame
from input_classes.human_interface import Human

class Game_State:

    def __init__(self, screen):
        self.world = screen

        # PROVISORISK STATE
        self.game_state = []
        """
        for lines in range(0, 10):
            line = []

            for tile in range(0, 10):
                curr_tile = (int(tile * 10 + self.world.board_offset_side),
                             int(lines * 10 + self.world.board_offset_top))
                line.append(curr_tile)

            self.game_state.append(line)
        """

    def start(self, screen, font):
        game_over = False
        clock = pygame.time.Clock()
        outcome = []

        interface = Human()

        while not game_over:

            """
            GÖR EN REQUEST FÖR ATT FÅ SE GAMESTATE
            """
            game_state = {
                "player1": [],
                "player2": [],
                "ball"   : []   
            }

            action = interface.get_action(self.game_state)

            if action == "Quit":
                game_over = True

            # Skicka req här för att få tillbaka mitt state efter min senaste action
            
            self.world.render(screen, font, self.game_state)

            clock.tick(5)
            
        return outcome
    
