from main.button import Button
from main.constants import *
from main.player import Player

player = Player()


class Game:
    def __init__(self):
        # initialize all buttons
        self.__buttons = []

        self.add_button(Button(400, 600, 400, 100, "Gather Resource: ", SCREEN, 'add_resource'))

        self.add_button(Button(400, 400, 400, 100, "Building 1: ", SCREEN, 'add_building'))

        # initialize building list
        self.__buildings = []

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_one = pygame.mouse.get_pressed()[0]
        for b in self.__buttons:
            b.update()
            if b.get_x() < mouse_x < b.get_x() + b.get_width() and b.get_y() < mouse_y < b.get_y() + b.get_height():
                if mouse_one:
                    if b.get_id() is 'add_resource':
                        player.modify_resources(player.get_resources_click())
                        print("Player has", player.get_total_resources(), "resources")

    def draw(self):
        for b in self.__buttons:
            b.draw()

    def get_button_list(self):
        return self.__buttons

    def add_button(self, btn):
        self.__buttons.append(btn)

    def delete_button(self, ind):
        self.__buttons.pop(ind)

    def add_building(self, bld):
        self.__buildings.append(bld)

    def delete_building(self, ind):
        self.__buildings.pop(ind)
