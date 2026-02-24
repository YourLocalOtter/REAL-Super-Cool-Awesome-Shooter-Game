import pygame


class Wall2:

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

    def display(self) -> None:
        rect_x = self.x - self.width / 2
        rect_y = self.y - self.height / 2
        pygame.draw.rect(self.surface, "#964B00", (rect_x, rect_y, self.width, self.height))


class PowerUp_ShootSpeed:

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
    
    def display(self) -> None:
        rect_x = self.x - self.width / 2
        rect_y = self.y - self.height / 2
        pygame.draw.circle(self.surface, "#FF21EA", (rect_x,rect_y), 20, width=0)