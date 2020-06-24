import pygame
import random
import time
import os
import math
os.environ["SDL_VIDEO_CENTERED"]='1'

#pygame configurations
width,height = 1200,500
fps= 60
pygame.display.set_caption("Fourier series")
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


white = (230, 230, 230)
black = (28, 28, 28)
gray = (100, 100, 100)

screen.fill(white)
pos_x = 250
pos_y = 200


N = 1
time= 0
radius = 120
offset = 300
wave_list = []
ITERATIONS = 10

run=True
while run:
    clock.tick(fps)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    x = pos_x
    y = pos_y
    for i in range(ITERATIONS):
        old_x = x
        old_y = y

        N = i * 2 + 1
        radius = 150 * (4/ (N * math.pi))
        x += int( radius * math.cos(N * time))
        y +=  int( radius * math.sin(N * time))


        pygame.draw.circle(screen, gray, (old_x, old_y), int(radius) ,2)

        pygame.draw.line(screen, black, (old_x, old_y), (x,y) , 3)
        pygame.draw.circle(screen, (50, 168, 66), (x,y), 5)

    wave_list.insert(0, y)
    if len(wave_list) > 1000:
        wave_list.pop()

    pygame.draw.line(screen, gray, (x,y), (pos_x+offset, wave_list[0]), 3)

    for index in range(len(wave_list)):
        pygame.draw.circle(screen, (149, 166, 151), (index + pos_x + offset, wave_list[index]), 3)
    time += 0.01

    pygame.display.update()

pygame.quit()