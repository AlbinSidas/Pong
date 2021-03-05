import pygame
from input_classes.human_interface import Human
import requests

class Game_State:

    def __init__(self, screen):
        self.world = screen
        self.game_state = self.world.game_board

    def start(self, screen, font):
        game_over = False
        clock = pygame.time.Clock()
        outcome = []

        interface = Human()

        while not game_over:

            action = interface.get_action(self.game_state)

            if action == "Quit":
                game_over = True

            # Skicka req här för att få tillbaka mitt state efter min senaste action
            state = requests.get("http://localhost:3000/move?action=" + str(action) + "id=" + self.world.identity)

            self.world.render(screen, font, self.game_state)
            clock.tick(5)
            
        return outcome