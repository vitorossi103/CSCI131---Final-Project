import pygame
from main import constants
from main import helpers


class Button:
    def __init__(self, x, y, width, height, text, screen, font='Arial'):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = text
        self.__screen = screen

        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(font, 24)

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.__screen, constants.BLACK, self.rect, 1)
        self.__draw_text()

    # todo: center text in rectangle
    def __draw_text(self):
        # self.__screen.blit(self.font.render(self.__text, True, constants.BLACK), (self.rect.centerx - 16,
        #                                                                           self.rect.centery))

        helpers.render_text(self.__text, self.font, self.rect, constants.BLACK, constants.BLACK)

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
