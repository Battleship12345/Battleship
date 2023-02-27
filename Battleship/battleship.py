import pygame
from sys import exit
from random import randint, choice

size = width, height = (600, 600)
fps = 30
 
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Battleship")
clock = pygame.time.Clock()



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, x2):
        super().__init__()
        self.y = y
        self.x = x
        self.width = x2
        self.image = pygame.Surface((self.width, 5))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft = (x,y))




while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    screen.fill("blue")
    
    pygame.display .update()
    clock.tick(fps)
