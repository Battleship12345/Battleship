import pygame
from sys import exit

size = width, height = (600, 600)
fps = 30

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, label):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))

        if label is not None:
            font = pygame.font.SysFont("arial", 16)
            text = font.render(label, True, (0, 0, 0))
            self.image.blit(text, (10, 10))

        pygame.draw.rect(self.image, (0, 0, 0), self.image.get_rect(), 1)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Squares Example")
clock = pygame.time.Clock()

squares = pygame.sprite.Group()


for i in range(0, 10):
    label = chr(ord('A') + i)
    square = Square((i + 1) * 40, 0, label)
    squares.add(square)


for x in range(0, 10):
    for y in range(1, 11):
        if x == 0:
            label = str(y)
            square = Square(0, y * 40, label)
            squares.add(square)
        square = Square(x * 40 + 40, y * 40, None)
        squares.add(square)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    squares.draw(screen)

    pygame.display.update()
    clock.tick(fps)
