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
OBJECT_MASS = 5
PLANET_SIZE = 50 # radius
OBJECT_SIZE = 5 # radius
VELOCITY_SCALE = 100
G = 5

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Slingshot Simulation")

background = pygame.transform.scale(pygame.image.load("img/background.jpg"), (WIN_WIDTH, WIN_HEIGHT))
planet_img = pygame.transform.scale(pygame.image.load("img/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

def main():
    clk = pygame.time.Clock()
    run = True

    objs = []
    tmp_obj_pos = None # stores position of object that has not been launched

    while run:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                tmp_obj_pos = mouse_pos

        window.blit(background, (0, 0))

        if tmp_obj_pos:
            pygame.draw.circle(window, RED, tmp_obj_pos, OBJECT_SIZE)

        pygame.display.update()

        clk.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
