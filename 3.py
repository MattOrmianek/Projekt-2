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
ITERATIONS = 5
#stworzyć kod na rysowanie całej funkcji 


pygame.quit()