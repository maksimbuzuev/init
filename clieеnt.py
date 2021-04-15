import pygame
import socket
import pickle

name = input("Имя: ")
soc = socket.socket()

soc.connect(("192.168.71.240", 5000))

sc = pygame.display.set_mode((600, 400))

image = pygame.image.load("image/idle.png")

data = {
    "name": name,
    "speed": 2,
    "x": 0,
    "y": 0
}

pygame.font.init()
f1 = pygame.font.Font(None, 16)

game = True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    soc.send(pickle.dumps(data))
    answer = soc.recv(4096)
    obj = pickle.loads(answer)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        data["y"] -= data["speed"]
    if keys[pygame.K_w]:
        data["y"] += data["speed"]
    if keys[pygame.K_w]:
        data["x"] -= data["speed"]
    if keys[pygame.K_w]:
        data["x"] += data["speed"]

    sc.fill((255, 255, 255))

    for player in obj:
        if "name" in obj[player]:
            n = f1.render(obj[player]["name"], True, (0, 0, 0))
            sc.blit(n, (obj[player]["x"], obj[player]["y"] - 20))
        sc.blit(image, (obj[player]["x"], obj[player]["y"]))

    pygame.display.update()
    pygame.time.delay(25)
