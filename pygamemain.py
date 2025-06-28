import pygame
import sys

pygame.init()

# name on the window
pygame.display.set_caption('Hivedle!')

# set screen size
screen = pygame.display.set_mode((1000, 1700))

# set a background
background = pygame.image.load("grid.png")

# colours 
white = (255, 255, 255)
green = (0, 200, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)
black = (0, 0, 0)

# text details
font = pygame.font.SysFont('arial', 150)
font2 = pygame.font.SysFont('arial', 75) 
user_input = ["", "", "", "", "", ""]
correct_word = "WORDL"
current_row = 0
# input should be always active
running = True
color = white
row_lock = [False] * 6
while running:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if not row_lock[current_row] and len(user_input[current_row]) > 0:
                    user_input[current_row] = user_input[current_row][:-1]
            elif event.key == pygame.K_RETURN:
                if len(user_input[current_row]) == 5:
                    row_lock[current_row] = True
                    if current_row < 5:
                        current_row += 1
            elif event.unicode.isalpha():
                if not row_lock[current_row] and len(user_input[current_row]) < 5:
                    user_input[current_row] += event.unicode.upper()
    for g in range(len(user_input)):
        word = user_input[g]
        for i in range(len(word)):
            letter = word[i]
            x = 56 + i * 183
            y = 170 + g * 208
            color = white
            if row_lock[g] and len(word) == 5:
                color = grey
                if letter == (correct_word[i]):
                    color = green
                elif letter in correct_word:
                    color = yellow
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 156, 156))
            text_surface = font.render(letter, True, black)
            text_rect = text_surface.get_rect(center = (x + 79, y + 85))
            screen.blit(text_surface, text_rect)
        if row_lock[5]:
            game_over = font2.render("GAME OVER!", True, black)
            screen.blit(game_over, (300, 50))



    screen.blit(background, (0, 0))
    pygame.display.update()
pygame.quit()
sys.exit()
