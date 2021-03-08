from input_classes.interface import Interface
import pygame

class Human(Interface):
    def __init__(self):
        self.key_converter = {
            1073741906 : "up",
            1073741905 : "down",
            1073741904 : "left",
            1073741903 : "right"
        }

    def get_action(self, world):
        key_l = []
        for event in pygame.event.get():
            pressed_key = "Not pressed"

            if event.type == pygame.locals.QUIT:
                return "Quit"   

            elif event.type == pygame.locals.KEYDOWN:
                pressed_key = event.key
            
            key_l.append(pressed_key)

        if len(key_l) == 0:
            key_l.append("Not pressed")

        action_list = list(filter(lambda x: x!="Not pressed", key_l))
        
        if len(action_list) == 0:
            return "Not pressed"
        else: 
            return self.key_converter.get(action_list[0], "Not pressed")
        