from main.button import Button
from main.constants import *


class Game:
    def __init__(self):
        self.__buttons = []

        self.add_button(Button(0, 0, 100, 100, "test", SCREEN, ''))
        self.add_button(Button(101, 0, 100, 200, "Gather Resource", SCREEN, ''))

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_one = pygame.mouse.get_pressed()[0]
        for b in self.__buttons:
            b.update()
            if b.get_x() < mouse_x < b.get_x() + b.get_width() and b.get_y() < mouse_y < b.get_y() + b.get_height():
                if mouse_one:
                    print("clicked button")

    def draw(self):
        for b in self.__buttons:
            b.draw()

    def get_button_list(self):
        return self.__buttons

    def add_button(self, btn):
        self.__buttons.append(btn)
