import pygame
import math
from settings import *

class Player:
    def __init__(self, color, speed, rotation_speed, position):
        self.color = PLAYER_COLOR
        self.speed = PLAYER_SPEED
        self.rotation_speed = PLAYER_ROTATION_SPEED
        self.x, self.y = PLAYER_POSITION_XY
        self.angle = 0
        self.radius = PLAYER_RADIUS

    def check_for_movement(self):
        sin_angle = math.sin(self.angle)
        cos_angle = math.cos(self.angle)
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.x += self.speed * cos_angle
            self.y += self.speed * sin_angle
        if key[pygame.K_s]:
            self.x -= self.speed * cos_angle
            self.y -= self.speed * sin_angle
        if key[pygame.K_a]:
            self.x += self.speed * sin_angle
            self.y -= self.speed * cos_angle
        if key[pygame.K_d]:
            self.x -= self.speed * sin_angle
            self.y += self.speed * cos_angle
        if key[pygame.K_LEFT]:
            self.angle -= self.rotation_speed
        if key[pygame.K_RIGHT]:
            self.angle += self.rotation_speed

    def check_boundaries(self):
        self.x = max(self.radius, min(self.x, WINDOW_WIDTH - self.radius))
        self.y = max(self.radius, min(self.y, WINDOW_HEIGHT - self.radius))

    def get_pos(self):
        return (self.x, self.y)
    
    def draw_player(self, window):
        pygame.draw.circle(window, self.color, (self.get_pos()), self.radius)

    def draw_ray(self, window):
        pygame.draw.line(window, self.color, (self.get_pos()), (self.x + WINDOW_WIDTH * math.cos(self.angle),
                                                                self.y + WINDOW_HEIGHT * math.sin(self.angle)))