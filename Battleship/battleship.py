import pygame
from sys import exit
from random import randint, choice

size = width, height = (800, 400)
fps = 30
 
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()


pygame.display .update()
clock.tick(fps)
