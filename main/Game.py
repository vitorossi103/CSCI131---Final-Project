from main.Button import Button
from main.constants import *


class Game:
    def __init__(self):
        self.__buttons = []

        self.add_button(Button(0, 0, 100, 100, "test", SCREEN))
        self.add_button(Button(0, 101, 100, 100, "test two", SCREEN))

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_one = pygame.mouse.get_pressed()[0]
        print(mouse_one)
        for b in self.__buttons:
            b.update()
            if b.get_x() < mouse_x < b.get_x() + b.get_width() and b.get_y() < mouse_y < b.get_y() + b.get_height():
                if mouse_one:
                    print("Button clicked")
                    
    def draw(self):
        for b in self.__buttons:
            b.draw()

    def get_button_list(self):
        return self.__buttons

    def add_button(self, btn):
        self.__buttons.append(btn)
