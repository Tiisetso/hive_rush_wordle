import pygame
import sys

pygame.init()

# name on the window
pygame.display.set_caption('Hivedle!')

# set screen size
screen = pygame.display.set_mode((1000, 1500))

# set a background
background = pygame.image.load("grid.png")

# colours 
white = (255, 255, 255)
green = (0, 200, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)
black = (0, 0, 0)

# text details
font = pygame.font.SysFont(None, 200)

user_input = ""
correct_word = "WORDL"
# input should be always active
running = True

while running:
    screen.fill(white)
    #screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif len(user_input) < 5 and event.unicode.isalpha():
                    user_input += event.unicode.upper()
    #screen.blit(background, (0, 0))
    # Drwing the letters and highlight blocks
    for i in range(len(user_input)):
        letter = user_input[i]
        x = 55 + i * 183
        y = 170
        color = grey
        if i < len (correct_word):
            if letter == correct_word[i]:
                color = green
            elif letter in correct_word:
                color = yellow
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 156, 156))
        text_surface = font.render(letter, True, black)
        text_rect = text_surface.get_rect(center = (x + 79, y +78))
        screen.blit(text_surface, text_rect)
    screen.blit(background, (0, 0))
    pygame.display.update()
pygame.quit()
sys.exit()

