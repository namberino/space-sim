import pygame
import math

# pygame constants
WIN_WIDTH, WIN_HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# simulation constants
PLANET_MASS = 100
SPACECRAFT_MASS = 5
PLANET_SIZE = 50 # radius
OBJECT_SIZE = 5 # radius
VELOCITY_SCALE = 100
G = 5

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Slingshot Simulation")

background_img = pygame.transform.scale(pygame.image.load("img/background.jpg"), (WIN_WIDTH, WIN_HEIGHT))
planet_img = pygame.transform.scale(pygame.image.load("img/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == "__main__":
    main()
