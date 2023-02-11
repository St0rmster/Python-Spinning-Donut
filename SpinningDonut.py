import pygame
import math

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
colums = WIDTH // x_separator
screen_size = rows * colums

x_offset = colums / 2
y_offset = rows / 2

A, B = 0, 0 # Rotating the Animation

theta_spacing = 10
phi_spacing = 1

chars = "_,-~:;=!*#$@" # luminance index

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_suface = pygame.display.set_mode((WIDTH, HEIGHT))
# display_suface = pygame.display.set_mode((0, 0), pygame,FULLSCREEN)
pygame.display.set_caption('Spinning Donut')
font = pygame.font.Sysfont('Arial', 18 , bold=True)


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, white)
    display_suface.blit(text, (x_start, y_start)) 

run = True
while run:

    screen.fill((black))

    z = [0] * screen_size
    b = [''] * screen_size

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.sin(A)
            h = d + 2
            D = 1 / (c * h * e + f * g * 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.cos(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n)) # 3D X coord after rotation
            y = int(y_offset + 20 * D * (l * h * m - t * n)) # 3D y coord after roatation
            o = int(x + colums * y) # 3D z coord after roation 
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f *g - l * d * n))
            if rows > y and y > 0 and x > 0 and colums > x and D > z[o]:
                z[o] = chars[N if N > 0 else 0]

if y_start == rows * y_separator - y_separator:
    y_start = 0

for i in range(len(b)):

    pygame.display.update()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

