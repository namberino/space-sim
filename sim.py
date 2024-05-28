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
SPACECRAFT_SIZE = 5 # radius
VELOCITY_SCALE = 100
G = 5

pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Slingshot Simulation")

background = pygame.transform.scale(pygame.image.load("img/background.jpg"), (WIN_WIDTH, WIN_HEIGHT))
planet_img = pygame.transform.scale(pygame.image.load("img/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

class Spacecraft:
    def __init__(self, x, y, xvel, yvel, mass):
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
        self.mass = mass

    def draw(self):
        pygame.draw.circle(window, RED, (int(self.x), int(self.y)), SPACECRAFT_SIZE)

def main():
    clk = pygame.time.Clock()
    run = True

    spacecrafts = []
    tmp_spacecraft_pos = None # stores position of object that has not been launched

    while run:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tmp_spacecraft_pos: # a spacecraft has already been placed
                    tmp_x, tmp_y = tmp_spacecraft_pos
                    craft = Spacecraft(tmp_x, tmp_y, 0, 0, SPACECRAFT_MASS)
                    spacecrafts.append(craft)
                    tmp_spacecraft_pos = None
                else:
                    tmp_spacecraft_pos = mouse_pos

        window.blit(background, (0, 0))

        if tmp_spacecraft_pos:
            pygame.draw.line(window, WHITE, tmp_spacecraft_pos, mouse_pos, 2) # draw line from object to mouse
            pygame.draw.circle(window, RED, tmp_spacecraft_pos, SPACECRAFT_SIZE)

        for craft in spacecrafts:
            craft.draw()

        pygame.display.update()

        clk.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
