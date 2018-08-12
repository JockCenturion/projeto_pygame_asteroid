
import pygame
from pygame.locals import *
from sys import exit 
from random import randrange

pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32)

pygame.display.set_caption("Kart")
clock 		= pygame.time.Clock()
background  = pygame.image.load("bg_big.png").convert()
ship        = pygame.image.load("ship.png").convert_alpha()
ship_position = [randrange(956), randrange(560)]




#______________________Funções___________________________
def create_asteroid():
	return {
		'surface' : pygame.image.load('asteroid.png').convert_alpha(),
		'position': [randrange(892), -64],
		'speed'   : randrange(10)
	}

def move_asteroids():
		for asteroid in asteroids:
			asteroid['position'][1] += asteroid['speed'];

def remove_used_asteroid():
	for asteroid in asteroids:
		if asteroid['position'][1] > 560:
			asteroids.remove(asteroid)
#______________________Jogo______________________________

ticks_to_asteroid = 90
asteroids = []

while True:

	if not ticks_to_asteroid:
		ticks_to_asteroid = 90
		asteroids.append(create_asteroid())
	else:
		ticks_to_asteroid -= 1

	speed = {
	'x': 0,
	'y': 0
	}

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[K_UP]:
		speed['y'] = -5
	elif pressed_keys[K_DOWN]:
		speed['y'] = 5
	elif pressed_keys[K_LEFT]:
		speed['x'] = -5
	elif pressed_keys[K_RIGHT]:
		speed['x'] = 5


	screen.blit(background, (0, 0))
	ship_position[0] += speed['x']
	ship_position[1] += speed['y']
	screen.blit(ship, ship_position)

	move_asteroids()

	for asteroid in asteroids:
		screen.blit(asteroid['surface'], asteroid['position'])

	pygame.display.update()
	time_passed = clock.tick(30)
	remove_used_asteroid()