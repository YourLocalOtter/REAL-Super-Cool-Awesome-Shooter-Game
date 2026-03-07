import pygame


class ShootingSpeed:

    def __init__(
        self,
        surface: pygame.Surface,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.width, self.height = width, height

    def update(self) -> None:
        return None

    def teleport_offscreen(self) -> None:
        self.x = -1000
        self.y = -1000

    def check_collision(self, x: float, y: float, width: float, height: float) -> bool:
        if (
            self.x < x + width / 2
            and self.x > x - width / 2
            and self.y < y + height / 2
            and self.y > y - height / 2
        ):
            return True
        return False

    def display(self) -> None:
        pygame.draw.circle(self.surface, "#FF007F", (int(self.x), int(self.y)), 20)
