import pygame
import sys
import random
import json
#import "filter_dict"
pygame.init()

# name on the window
pygame.display.set_caption('Hivedle!')

# set screen size
screen = pygame.display.set_mode((530, 900))

# set a background
background = pygame.image.load("grid.png")

# colours 
white = (255, 255, 255)
green = (0, 200, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)
black = (0, 0, 0)

# text details
font = pygame.font.SysFont('arial', 88)
font2 = pygame.font.SysFont('arial', 50)
user_input = ["", "", "", "", "", ""]
#correct_word = get_random_word_from_dict("filtered.json")

current_row = 0
# input should be always active
running = True
color = white
row_lock = [False] * 6

#random function to choose word for the game
def get_random_word_from_list(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    
    # Extract the keys (the words)
    word_list = list(data.keys())

    # Choose a random one
    return random.choice(word_list).upper()

correct_word = get_random_word_from_list("filtered.json")
print(correct_word)

# search that the word is part of the list
def word_is_valid(user_input, filename = "filtered.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
        return user_input.lower() in data

# Game Over text
win = False

while running:
    screen.fill(white)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            break
        
        if win or row_lock[5]:
            continue
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if not row_lock[current_row] and len(user_input[current_row]) > 0:
                    user_input[current_row] = user_input[current_row][:-1]
            
            elif event.key == pygame.K_RETURN:
                current_word = user_input[current_row]
                if len(current_word) == 5:
                    if word_is_valid(current_word):
                        row_lock[current_row] = True
                        
                        if current_word == correct_word:
                            win = True

                        if current_row < 5:
                            current_row += 1
            
            elif event.unicode.isalpha():
                if not row_lock[current_row] and len(user_input[current_row]) < 5:
                    user_input[current_row] += event.unicode.upper()
    for g in range(len(user_input)):
        word = user_input[g]
        for i in range(len(word)):
            letter = word[i]
            x = 11 + i * 104
            y = 117 + g * 104
            color = white
            if row_lock[g] and len(word) == 5:
                color = grey
                if letter == (correct_word[i]):
                    color = green
                elif letter in correct_word:
                    color = yellow
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 89, 89))
            text_surface = font.render(letter, True, black)
            text_rect = text_surface.get_rect(center = (x + 45, y + 45))
            screen.blit(text_surface, text_rect)

    screen.blit(background, (0, 0))
    if win:
        win_text = font2.render("WELL JOB!", True, black)
        screen.blit(win_text, (135, 40))
    elif row_lock[5]:
        game_over = font2.render("GAME OVER!", True, black)
        screen.blit(game_over, (115, 40))
    pygame.display.update()
pygame.quit()
sys.exit()
