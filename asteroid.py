import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        big_split_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid_velocity = self.velocity.rotate(random_angle)
        second_asteroid_velocity = self.velocity.rotate(-random_angle)
        og_x = self.position.x
        og_y = self.position.y
        split_one = Asteroid(og_x, og_y, big_split_radius)
        split_two = Asteroid(og_x, og_y, ASTEROID_MIN_RADIUS)
        split_one.velocity = first_asteroid_velocity * 1.2
        split_two.velocity = second_asteroid_velocity * 1.2
