from input_classes.interface import Interface
import pygame

class Human(Interface):
    def __init__(self):
        pass

    def get_action(self, world):
        key_l = []
        for event in pygame.event.get():
            pressed_key = "Not pressed"

            if event.type == pygame.locals.QUIT:
                pressed_key = "Quit"                
            elif event.type == pygame.locals.KEYDOWN:
                pressed_key = event.key
            
            key_l.append(pressed_key)

        if len(key_l) == 0:
            key_l.append("Not pressed")

        action_list = list(filter(lambda x: x!="Not pressed", key_l))
        
        if len(action_list) == 0:
            return "Not pressed"
        else: 
            return action_list[0]
        