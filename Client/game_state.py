import pygame

class Game_State:

    def __init__(self, screen):
        #self.world = game_world.World(config)
        #self.world_list = self.world.world
        #self.python = snake.Snake(self.world_list, config)

        self.world = screen

        #etc

        # screen = screen_window # as this should be the same screen as world is written at
        # world = worldobject
        # snake = snake
        # fruit = fruit

    def start(self, screen, font):
        #gameloop
        game_over = False
        clock = pygame.time.Clock()
        fruit_list = []
        key_l = []
        outcome = []

        #interface = Agent_Interface(Human())
        #interface = Agent_Interface(AStar(self.world_list))
        #interface = Agent_Interface(Hamilton(self.world_list))


        while not game_over:
            """
            if len(fruit_list) == 0:
                self.place_fruit(self.world_list, self.python, fruit_list)
            
            self.world.render(screen, self.world_list, self.python, fruit_list, font)

            action = interface.get_action(self.world_list, self.python, fruit_list[0], pygame)
            """

            action = interface.get_action(game_state)

            if action == "Quit":
                game_over = True
            
            #clock.tick(8)
            #clock.tick(20)
            
            #self.python.update(action, self.world_list, fruit_list)

            if ball_in_goal:
                game_over = True

        return outcome
    