import pygame
from input_classes.human_interface import Human
import requests
import json

class Game_State:

    def __init__(self, screen):
        self.world = screen


    def start(self, screen, font):
        game_over = False
        clock = pygame.time.Clock()
        outcome = []

        interface = Human()

        while not game_over:
            action = interface.get_action(self.world.game_board)

            if action == "Quit":
                game_over = True

            # Skicka req här för att få tillbaka mitt state efter min senaste action
            response = requests.get("http://ec2-13-49-15-244.eu-north-1.compute.amazonaws.com:3000/move?action=" + str(action) + "&id=" + self.world.identity)
            state = json.loads(response.text)

            self.world.game_board.update(state['gameBoard'], state['entities'])
            
            self.world.render(screen, font, True)

            # Denna bestämmer hur ofta klienten skicar requests mot servern
            clock.tick(5)
            
        return outcome