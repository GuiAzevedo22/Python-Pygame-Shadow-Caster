import pygame
import math
from settings import *
from player import *

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
my_player = Player(GREY, PLAYER_SPEED, PLAYER_ROTATION_SPEED, PLAYER_POSITION_XY)

def draw():
    window.fill((GREY))
    #draw_grid()
    my_player.draw_player(window)
    my_player.draw_ray(window)

def event_handler():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

run = True
while(run):
    event_handler()
    my_player.check_for_movement()
    my_player.check_boundaries()
    draw()
    clock.tick(FPS)
    pygame.display.set_caption(TITLE + str(round(clock.get_fps())))
    pygame.display.update()
              
pygame.quit()