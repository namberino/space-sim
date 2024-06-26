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
distance_font = pygame.font.SysFont("Arial", 15)

class Planet:
    def __init__(self, x, y, radius, mass, color, name):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color
        self.name = name
        self.xvel = 0
        self.yvel = 0
        self.sun = False
        self.distance_to_sun = 0
        self.orbit_points = []

    def draw(self):
        scaled_x = self.x * SCALE + WIN_WIDTH / 2
        scaled_y = self.y * SCALE + WIN_HEIGHT / 2

        if len(self.orbit_points) > 2:
            updated_points = []
            for point in self.orbit_points:
                orbit_x, orbit_y = point
                orbit_x = orbit_x * SCALE + WIN_WIDTH / 2
                orbit_y = orbit_y * SCALE + WIN_HEIGHT / 2
                updated_points.append((orbit_x, orbit_y))
            pygame.draw.lines(window, self.color, False, updated_points, 2)

        pygame.draw.circle(window, self.color, (scaled_x, scaled_y), self.radius)

        if not self.sun:
            color_text = distance_font.render(f"{self.name}", 1, WHITE)
            window.blit(color_text, (scaled_x - color_text.get_width() / 2, scaled_y - color_text.get_height()))
            distance_text = distance_font.render(f"{round(self.distance_to_sun / 1000, 2)}km", 1, WHITE)
            window.blit(distance_text, (scaled_x - distance_text.get_width() / 2, scaled_y - distance_text.get_height() / 5))

    def attraction(self, other):
        other_x, other_y = other.x, other.y

        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        force = (G * self.mass * other.mass) / distance**2
        theta_angle = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta_angle) * force
        force_y = math.sin(theta_angle) * force

        return force_x, force_y

    def update_pos(self, planets):
        total_force_x = 0
        total_force_y = 0

        for planet in planets:
            if self == planet:
                continue

            # calculate force on current planet by every other planets
            force_x, force_y = self.attraction(planet)
            total_force_x += force_x
            total_force_y += force_y

        self.xvel += total_force_x / self.mass * TIMESTEP
        self.yvel += total_force_y / self.mass * TIMESTEP

        self.x += self.xvel * TIMESTEP
        self.y += self.yvel * TIMESTEP

        self.orbit_points.append((self.x, self.y))
        if len(self.orbit_points) > 680:
            self.orbit_points.pop(0)

def main():
    run = True
    clk = pygame.time.Clock()

    sun = Planet(0, 0, 30, 1.98892 * 10**30, YELLOW, "Sun")
    sun.sun = True

    mercury = Planet(0.387 * ASTRONOMICAL_UNIT, 0, 8, 3.30 * 10**23, DARK_GREY, "Mercury")
    mercury.yvel = -47.4 * 1000

    venus = Planet(0.723 * ASTRONOMICAL_UNIT, 0, 14, 4.8685 * 10**24, WHITE, "Venus")
    venus.yvel = -35.02 * 1000

    earth = Planet(-1 * ASTRONOMICAL_UNIT, 0, 16, 5.9742 * 10**24, BLUE, "Earth")
    earth.yvel = 29.783 * 1000

    mars = Planet(-1.524 * ASTRONOMICAL_UNIT, 0, 12, 6.39 * 10**23, RED, "Mars")
    mars.yvel = 24.077 * 1000

    planets = [sun, mercury, venus, earth, mars]

    while (run):
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        for planet in planets:
            planet.update_pos(planets)
            planet.draw()

        pygame.display.update()
        clk.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
