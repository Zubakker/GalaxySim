import pygame
import json
import time
from math import sqrt, atan2

def sign(x):
    return (1 if x >= 0 else -1)

pygame.init()
screen = pygame.display.set_mode((600, 500))
FONT = pygame.font.SysFont("SOURCECODE PRO", 10)

OBJECTS = open("OBJECTS.json", "r").read()
OBJECTS = json.loads(OBJECTS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 500:
                OBJECTS = open("OBJECTS.json", "r").read()
                OBJECTS = json.loads(OBJECTS)


    for obj in OBJECTS:
        for sobj in OBJECTS:
            dx = (obj["COORDS"][0] - sobj["COORDS"][0]) 
            dy = (obj["COORDS"][1] - sobj["COORDS"][1]) 
            if dx != 0 and dy != 0:
                force = sobj["MASS"] / (dx ** 2 + dy ** 2)
                k = sqrt(force / (dx ** 2 + dy ** 2))
                forcex = dx * k
                forcey = dy * k
            else:
                forcex, forcey, force = 0, 0, 0
            obj["SPEED"][0] += (forcex)
            obj["SPEED"][1] += (forcey)
            if abs(obj["SPEED"][0]) > 30:
                obj["SPEED"][0] == 30 * sign(obj["SPEED"][0])
            if abs(obj["SPEED"][1]) > 30:
                obj["SPEED"][1] == 30 * sign(obj["SPEED"][1])
            if (dx * dx + dy * dy < (obj["SIZE"] + sobj["SIZE"]) ** 2 and \
                    obj["COORDS"] != sobj["COORDS"]):
                obj["SPEED"] = [0, 0]
        obj["COORDS"][0] -= (obj["SPEED"][0]) / 10
        obj["COORDS"][1] -= (obj["SPEED"][1]) / 10

    screen.fill((0, 0, 30))
    pygame.draw.rect(screen, (60, 0, 0), (500, 0, 100, 500))
    screen.blit(FONT.render("Click here",  0, (100, 100, 100)), (500, 5))
    screen.blit(FONT.render("to refresh",  0, (100, 100, 100)), (500, 20))

    for i in range(len(OBJECTS)):
        obj = OBJECTS[i]
        pygame.draw.circle(screen, (0, 0, 60), (int(obj["COORDS"][0]),
                    int(obj["COORDS"][1])), int(obj["SIZE"]))
        pygame.draw.circle(screen, (0, 0, 0), (int(obj["COORDS"][0]),
                    int(obj["COORDS"][1])), int(obj["SIZE"]) + 1, 1)
        if obj["MASS"] > 2:
            pygame.draw.circle(screen, (0, 60, 0), (int(obj["COORDS"][0]),
                        int(obj["COORDS"][1])), int(obj["MASS"]) + 1, 2)
        pygame.draw.line(screen, (60, 0, 0), (int(obj["COORDS"][0]),
            int(obj["COORDS"][1])), (int(obj["COORDS"][0] - obj["SPEED"][0]),
                int(obj["COORDS"][1] - obj["SPEED"][1])), 2)
        screen.blit(FONT.render("OBJ " + str(i), 0, (100, 100, 100)), 
                    (int(obj["COORDS"][0]), int(obj["COORDS"][1])))
    pygame.display.update()
    time.sleep(0.01)



