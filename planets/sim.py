import pygame
import math

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

ASTRONOMICAL_UNIT = 149.6e6 * 1000 # distance of earth from the sun
SCALE = 220 / ASTRONOMICAL_UNIT # scaling down the distance since space is HUGE (1 AU = 100 px)
TIMESTEP = 3600 * 24 # 1 day
G = 6.67428e-11 # gravitational constant

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 800, 800
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Planets Simulation")
sim_font = pygame.font.SysFont("Arial", 16)

class Planet:
    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color
        self.xvel = 0
        self.yvel = 0
        self.sun = False
        self.distance_to_sun = 0
        self.orbit_points = []

    def draw(self):
        scaled_x = self.x * SCALE + WIN_WIDTH / 2
        scaled_y = self.y * SCALE + WIN_HEIGHT / 2

        pygame.draw.circle(window, self.color, (scaled_x, scaled_y), self.radius)


def main():
    run = True
    clk = pygame.time.Clock()

    sun = Planet(0, 0, 30, 1.98892 * 10**30, YELLOW)
    sun.sun = True

    mercury = Planet(0.387 * ASTRONOMICAL_UNIT, 0, 8, 3.30 * 10**23, DARK_GREY)
    mercury.yvel = -47.4 * 1000

    venus = Planet(0.723 * ASTRONOMICAL_UNIT, 0, 14, 4.8685 * 10**24, WHITE)
    venus.yvel = -35.02 * 1000

    earth = Planet(-1 * ASTRONOMICAL_UNIT, 0, 16, 5.9742 * 10**24, BLUE)
    earth.yvel = 29.783 * 1000

    mars = Planet(-1.524 * ASTRONOMICAL_UNIT, 0, 12, 6.39 * 10**23, RED)
    mars.yvel = 24.077 * 1000

    planets = [sun, mercury, venus, earth, mars]

    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        for planet in planets:
            planet.draw()

        pygame.display.update()
        clk.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
