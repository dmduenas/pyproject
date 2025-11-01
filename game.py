import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200)) #create the regular surface
test_surface.fill("Red")

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))#this means in the screen surface, place test_surface in the 0,0 coordinates
    #block image transfer. fancy way of saying you want to put one surface on another surface


    pygame.display.update()
    clock.tick(60)
