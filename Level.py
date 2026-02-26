import pygame

pygame.init()
pygame.font.init()

from wall import Wall


class Level:
    def __init__(self, surface: pygame.Surface, level_num: int = 1) -> None:
        self.surface = surface
        self.walls = []
        self.level_num = level_num
        self.load_level(level_num)

    def load_level(self, level_num: int) -> None:
        self.walls = []
        screen_width = self.surface.get_width()
        screen_height = self.surface.get_height()

        if level_num == 1:
            self.walls.append(
                Wall(self.surface, 0.25 * screen_width, screen_height / 2, 30, 130)
            )
            self.walls.append(
                Wall(self.surface, 0.75 * screen_width, screen_height / 2, 30, 130)
            )
        elif level_num == 2:
            self.walls.append(
                Wall(self.surface, 0.5 * screen_width, screen_height / 3.8, 30, 160)
            )
            self.walls.append(
                Wall(self.surface, 0.5 * screen_width, screen_height / 1.28, 30, 160)
            )
        elif level_num == 3:
            for i in range(1, 4):
                self.walls.append(
                    Wall(
                        self.surface,
                        0.25 * screen_width * i,
                        screen_height / 2,
                        30,
                        100,
                    )
                )

    def add_wall(self, wall: "Wall") -> None:
        self.walls.append(wall)

    def get_walls(self) -> list:
        return self.walls
