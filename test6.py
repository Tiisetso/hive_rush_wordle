import pygame

pygame.init()


# Define rgb values

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
position = (0,0)
position2 = (110,110)


# assigning coordinates
X = 700
Y = 700

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Show Text')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render('I am WORDLE', True, green, blue)

textRect = text.get_rect()
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)


# CREATING CANVAS
canvas = pygame.display.set_mode((1000,1000))

# TITLE OF CANVAS
pygame.display.set_caption("Show Image")

image = pygame.image.load("hexagon.jpg")
exit = False

#display_surface.blit(text, textRect)
while not exit:
    canvas.fill(white)
    canvas.blit(image, dest = position)
    canvas.blit(text, dest = position2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
