import pygame

class PowerUp_OtherPlayerFreeze:

    def __init__(self, surface: pygame.Surface, x: float, y: float, width: float, height: float) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.width, self.height = width, height

    def teleport_offscreen(self):
        self.x = -1000
        self.y = -1000

    def check_collision(self, x, y, width, height):
        if (
            self.x < x + width/2 and
            self.x > x - width/2 and
            self.y < y + height/2 and
            self.y > y - height/2
        ):
            return True
        return False

    def update(self) -> None:
        return None
    
    def display(self) -> None:
        pygame.draw.circle(self.surface, "#66FF00", (int(self.x), int(self.y)), 20)
        