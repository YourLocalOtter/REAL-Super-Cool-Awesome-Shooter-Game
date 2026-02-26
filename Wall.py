import pygame

pygame.init()


class Wall:
    def __init__(
        self, surface: pygame.Surface, x: float, y: float, width: float, height: float
    ) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.width, self.height = width, height

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(
            int(self.x - self.width / 2),
            int(self.y - self.height / 2),
            int(self.width),
            int(self.height),
        )

    def update(self) -> None:
        return None

    def display(self) -> None:
        r = self.get_rect()
        pygame.draw.rect(self.surface, "#964B00", r)
