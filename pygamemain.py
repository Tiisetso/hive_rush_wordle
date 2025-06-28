import pygame
import sys

pygame.init()

# name on the window
pygame.display.set_caption('Hivedle!')

# set screen size
screen = pygame.display.set_mode((1000, 1500))

# set a background
background = pygame.image.load("grid.png")
exit = False

# colours 
white = (255, 255, 255)
green = (0, 200, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)
black = (0, 0, 0)
colour = white
# positions
X = 140
Y = 250
position1 = (0,0)
position2 = (X, Y)

# text details
font = pygame.font.SysFont(None, 200)
input_text = ''
correct_letter = "A"
correctish_letter = "Z"
#letter_indent = letter_surface.get_rect(center = position2)

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
                if len(input_text) < 1 and event.unicode.isalpha():
                    input_text += event.unicode.upper()

    
    screen.fill(white)
    screen.blit(background, dest = position1)
    if input_text == correct_letter:
        pygame.draw.rect(screen, green, pygame.Rect(56, 169, 158, 157))
    elif input_text == correctish_letter: 
        pygame.draw.rect(screen, yellow, pygame.Rect(56, 169, 158, 157))
    pygame.draw.rect(screen, colour, pygame.Rect(239, 169, 158, 157))
    pygame.draw.rect(screen, colour, pygame.Rect(421, 169, 158, 157))
    pygame.draw.rect(screen, colour, pygame.Rect(604, 169, 158, 157))
    pygame.draw.rect(screen, colour, pygame.Rect(786, 169, 158, 157))
    #screen.blit(text_surface, dest = position2) 
    text_surface = font.render(input_text, True, black)
    text_rect = text_surface.get_rect(center = position2)
    screen.blit(text_surface, text_rect)
    pygame.display.update()
