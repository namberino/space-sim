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
G = 24.79

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

    def move(self, planet=None):
        distance = math.sqrt((self.x - planet.x) ** 2 + (self.y - planet.y) ** 2)
        force = (G * self.mass * planet.mass) / distance ** 2
        accel = force / self.mass
        theta_angle = math.atan2(planet.y - self.y, planet.x - self.x)
        accel_x = math.cos(theta_angle) * accel
        accel_y = math.sin(theta_angle) * accel

        print(accel_x, accel_y)

        self.xvel += accel_x
        self.yvel += accel_y

        self.x += self.xvel
        self.y += self.yvel

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self):
        window.blit(planet_img, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))

def create_spacecraft(location, mouse_pos):
    tmp_x, tmp_y = location
    mouse_x, mouse_y = mouse_pos

    # simple square triangle calculation (with velocity scaling)
    xvel = (mouse_x - tmp_x) / VELOCITY_SCALE
    yvel = (mouse_y - tmp_y) / VELOCITY_SCALE

    craft = Spacecraft(tmp_x, tmp_y, xvel, yvel, SPACECRAFT_MASS)

    return craft

def main():
    clk = pygame.time.Clock()
    run = True

    planet = Planet(WIN_WIDTH // 2, WIN_HEIGHT // 2, PLANET_MASS)
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
                    craft = create_spacecraft(tmp_spacecraft_pos, mouse_pos)
                    spacecrafts.append(craft)
                    tmp_spacecraft_pos = None
                else:
                    tmp_spacecraft_pos = mouse_pos

        window.blit(background, (0, 0))

        if tmp_spacecraft_pos:
            pygame.draw.line(window, WHITE, tmp_spacecraft_pos, mouse_pos, 2) # draw line from object to mouse
            pygame.draw.circle(window, RED, tmp_spacecraft_pos, SPACECRAFT_SIZE)

        for craft in spacecrafts.copy():
            craft.draw()
            craft.move(planet)

            collided = math.sqrt((craft.x - planet.x) ** 2 + (craft.y - planet.y) ** 2) <= PLANET_SIZE # difference between 2 points

            # remove offscreen spacecrafts
            if craft.x < 0 or craft.x > WIN_WIDTH or craft.y < 0 or craft.y > WIN_HEIGHT or collided:
                spacecrafts.remove(craft)

        planet.draw()

        pygame.display.update()

        clk.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
