import pygame
from random import randrange

RES = 800
SIZE = 500

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {"W": True, "S": True, "A": True, "D": True, }
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, SIZE])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color("black"))
    [(pygame.draw.rect(sc, pygame.Color("green"), (dx, dy, 64, 64))) for dx, xy in snake]
    pygame.draw.rect(sc, pygame.Color("red"), (*apple, SIZE, SIZE))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE)
        length += 1
        fps += 1

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE:

        if len(snake) != len(set(snake))


    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs["W"]:
        dx, dy = 0, -1
        dirs = {"W": True, "S": False, "A": True, "D": True, }
    if key[pygame.K_s] and dirs["S"]:
        dx, dy = 0, 1
        dirs = {"W": False, "S": True, "A": True, "D": True, }
    if key[pygame.K_a] and dirs["A"]:
        dx, dy = -1, 0
        dirs = {"W": True, "S": True, "A": True, "D": False, }
    if key[pygame.K_d] and dirs["D"]:
        dx, dy = 1, 0
        dirs = {"W": True, "S": True, "A": False, "D": True, }
