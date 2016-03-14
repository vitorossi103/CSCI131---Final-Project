import pygame
import sys

from main import constants
from main.Game import Game, SCREEN
from main.Button import Button

pygame.init()
clock = pygame.time.Clock()

game = Game()

while True:
	for e in pygame.event.get():
		if e.type is pygame.QUIT:
			sys.exit()

	game.update()

	SCREEN.fill(constants.WHITE)

	game.draw()

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
