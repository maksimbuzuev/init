import pygame

sc = pygame.display.set_mode((400, 400))

X = 100
Y = 100


playerImage = pygame.image.load("images.png")

playerImage = pygame.transform.scale(playerImage, (60, 60))


game = True
map = (
     (1,1,0,0,0,0,0,0,0,0,0,0,0,0,0),
     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
)





while game:



    for i in pygame.event.get():
        print(i)
        if i.type == pygame.TEXTINPUT:
            if i.text == "s":
                Y += 3
            if i.text == "w":
                Y -= 3
            if i.text == "a":
                X -= 3
            if i.text == "d":
                X += 3


        if i.type == pygame.QUIT:
            game = False


    sc.fill((255,255,255))
     for i, list in enumerate(map):
         for J, pos in enumerate(list):
            if pos == 0:
                pygame.draw.rect(sc, (255, 0, 0), (j * 40, i * 40, 40, 40))
            if pos == 1:
                pygame.draw.rect(sc, (0, 0, 255), (j * 40, i * 40, 40, 40))


    sc.blit(playerImage, (X, Y))
    pygame.display.update()
    pygame.time.delay(30)






