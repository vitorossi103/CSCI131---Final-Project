import main
from main import helpers
from main.constants import *


class Button:
    def __init__(self, x, y, width, height, text, screen, button_id, font='Arial'):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__screen = screen
        self.__id = button_id

        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(font, 24)
        self.player = main.game.player

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.__screen, BLACK, self.rect, 1)
        self.__draw_text()

    # todo: fix text rendering
    def __draw_text(self):
        if self.__id is 'add_resource':
            helpers.render_text(self.__text + str(self.player.get_total_resources()), self.font, self.rect, BLACK, 0)
        elif self.__id is 'add_building':
            pass

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_text(self):
        return self.__text

    def get_id(self):
        return self.__id
