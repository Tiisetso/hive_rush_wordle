import pygame
import sys

pygame.init()

# name on the window
pygame.display.set_caption('Hivedle!')

# set screen size
screen = pygame.display.set_mode((1000, 1000))

# set a background
background = pygame.image.load("hexagons.png")
exit = False

# colours 
white = (255, 255, 255)
green = (0, 200, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)
black = (0, 0, 0)
colour = white
# positions
X = 500
Y = 500
position1 = (0,0)
position2 = (175,175)

# text details
font = pygame.font.SysFont(None, 200)
input_text = ''
# input should be always active
active = True

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len(input_text) < 5 and event.unicode.isalpha():
                    input_text += event.unicode.upper()

    
    #screen.fill(white)
    screen.blit(background, dest = position1)
    text_surface = font.render(input_text, True, black)

    pygame.draw.rect(screen, colour, pygame.Rect(100, 100, 150, 150))
    pygame.draw.rect(screen, colour, pygame.Rect(270, 100, 150, 150))
    pygame.draw.rect(screen, colour, pygame.Rect(440, 100, 150, 150))
    pygame.draw.rect(screen, colour, pygame.Rect(610, 100, 150, 150))
    pygame.draw.rect(screen, colour, pygame.Rect(780, 100, 150, 150))
    screen.blit(text_surface, dest = position2)
    letter_surface = font.render('W', True, green)
    letter_rect = letter_surface.get_rect(center=position2)
    screen.blit(letter_surface, letter_rect)

    pygame.display.update()
