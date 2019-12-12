import json
import pygame
from math import sqrt

pygame.init()
screen = pygame.display.set_mode((600, 500))
stage = "COORDS_GRAPH"
stage_ans = {"COORDS": "Type in object coordinates",
             "SIZE":   "Type in object size",
             "MASS":   "Type in object mass",
             "SPEED":  "Type in object horizontal, vertical speed"}
nstages = {"COORDS": "SIZE",
           "SIZE": "MASS",
           "MASS": "SPEED",
           "SPEED": "COORDS"}

OBJECTS = open("OBJECTS.json", "r").read()
OBJECTS = json.loads(OBJECTS)
FONT = pygame.font.SysFont("SOURCECODE PRO", 10)
BIG_FONT = pygame.font.SysFont("SOURCECODE PRO", 25)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 500:
                stage = stage.strip("_GRAPH")
            if stage == "COORDS_GRAPH":
                coords = event.pos
                stage = "SIZE_GRAPH"

            elif stage == "SIZE_GRAPH":
                size = sqrt((coords[0] - event.pos[0]) ** 2 
                             + (coords[1] - event.pos[1]) ** 2)
                stage = "MASS_GRAPH"

            elif stage == "MASS_GRAPH":
                mass = sqrt((coords[0] - event.pos[0]) ** 2 
                             + (coords[1] - event.pos[1]) ** 2)
                stage = "SPEED_GRAPH"

            elif stage == "SPEED_GRAPH":
                speed = coords[0] - event.pos[0], coords[1] - event.pos[1]
                OBJECTS.append({"COORDS": coords,
                             "SIZE":   size,
                             "MASS":   mass,
                             "SPEED":  speed})
                outp = open("OBJECTS.json", "w")
                outp.write(json.dumps(OBJECTS))
                outp.close()
                stage = "COORDS_GRAPH"



    
    if stage in stage_ans:
        print(stage_ans[stage], ": ", sep="", flush=True, end="")
        ans = input()
        try:
            if ans == "DELETE":
                print("WHICH ONE?", end=" ", flush=True)
                n = int(input())
                del OBJECTS[n]
                outp = open("OBJECTS.json", "w")
                outp.write(json.dumps(OBJECTS))
                outp.close()
                stage = "COORDS_GRAPH"

            ans = [int(x) for x in ans.split()]
            if stage == "COORDS":
                coords = (ans[0], ans[1])
            if stage == "SIZE":
                size = ans[0]
            if stage == "MASS":
                mass = ans[0]
            if stage == "SPEED":
                speed = ans[0], ans[1]
                OBJECTS.append({"COORDS": coords,
                             "SIZE":   size,
                             "MASS":   mass,
                             "SPEED":  speed})
                outp = open("OBJECTS.json", "w")
                outp.write(json.dumps(OBJECTS))
                outp.close()
            stage = nstages[stage] + "_GRAPH"
        except Exception:
            print("THERE WAS A MISTAKE")

    screen.fill((0, 0, 30))
    pygame.draw.rect(screen, (60, 0, 0), (500, 0, 100, 500))
    screen.blit(FONT.render("Click here", 0, 
            (100, 100, 100)), (502, 5))
    screen.blit(FONT.render("to type-in", 0, 
            (100, 100, 100)), (502, 17))
    screen.blit(FONT.render("numbers", 0, 
            (100, 100, 100)), (502, 29))
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


    if stage == "COORDS_GRAPH":
        pygame.draw.circle(screen, (0, 0, 100), pygame.mouse.get_pos(), 14)
        pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 
                               15, 1)
        screen.blit(BIG_FONT.render("Select coordinates", 0, 
                    (100, 100, 100)), (5, 500 - 40))
    if stage == "SIZE_GRAPH":
        radius = sqrt((coords[0] - pygame.mouse.get_pos()[0]) ** 2 
                        + (coords[1] - pygame.mouse.get_pos()[1]) ** 2)
        pygame.draw.circle(screen, (0, 0, 100), coords, int(radius))
        pygame.draw.circle(screen, (0, 0, 0), coords, int(radius + 1), 1)
        screen.blit(BIG_FONT.render("Select size", 0, 
                    (100, 100, 100)), (5, 500 - 40))
        
    if stage == "MASS_GRAPH":
        massive = sqrt((coords[0] - pygame.mouse.get_pos()[0]) ** 2 
                        + (coords[1] - pygame.mouse.get_pos()[1]) ** 2)
        pygame.draw.circle(screen, (0, 0, 100), coords, int(size))
        pygame.draw.circle(screen, (0, 0, 0), coords, int(size), 1)
        pygame.draw.circle(screen, (0, 80, 0), coords, int(massive), 2)
        screen.blit(BIG_FONT.render("Select mass", 0, 
                    (100, 100, 100)), (5, 500 - 40))

    if stage == "SPEED_GRAPH":
        pygame.draw.circle(screen, (0, 0, 100), coords, int(size))
        pygame.draw.circle(screen, (0, 0, 0), coords, int(size), 1)
        if mass > 2:
             pygame.draw.circle(screen, (0, 80, 0), coords, int(mass), 2)
        pygame.draw.line(screen, (80, 0, 0), coords, pygame.mouse.get_pos(), 2)
        screen.blit(BIG_FONT.render("Select speed vector", 0, 
                    (100, 100, 100)), (5, 500 - 40))



    pygame.display.update()

