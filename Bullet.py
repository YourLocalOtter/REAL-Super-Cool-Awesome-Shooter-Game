import pygame

pygame.init()
from wall import Wall


class Bullet:

    def __init__(
        self, surface: pygame.Surface, x: float, y: float, vx: float, vy: float
    ) -> None:
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = 5

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            int(self.radius * 2),
            int(self.radius * 2),
        )

    def teleport_offscreen(self) -> None:
        self.x = -1000
        self.y = -1000

    def update(self, walls: list[Wall]) -> bool:
        self.x += self.vx
        self.y += self.vy

        brect = self.get_rect()
        for wall in walls:
            if brect.colliderect(wall.get_rect()):
                self.teleport_offscreen()
                return False

        if (
            self.x - self.radius < 0
            or self.x + self.radius > self.surface.get_width()
            or self.y - self.radius < 0
            or self.y + self.radius > self.surface.get_height()
        ):
            return False

        return True

    def display(self) -> None:
        pygame.draw.circle(
            self.surface, "#ffffff", (int(self.x), int(self.y)), self.radius
        )

    def check_collision(self, x: float, y: float, width: float, height: float) -> bool:
        if (
            self.x - self.radius < x + width / 2
            and self.x + self.radius > x - width / 2
            and self.y - self.radius < y + height / 2
            and self.y + self.radius > y - height / 2
        ):
            return True
        return False
