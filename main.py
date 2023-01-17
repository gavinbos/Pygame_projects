import pygame

# Make sure to add this line to initialize pygame at the beginning of each file
pygame.init()

# create game window
screen = pygame.display.set_mode( (800, 600) )

# Title and Icon of window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('SpaceShip.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('Player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))
    # blit is essentially a draw method

# main game loop
running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player()
    pygame.display.update()