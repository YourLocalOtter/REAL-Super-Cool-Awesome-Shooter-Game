import pygame

pygame.init()
pygame.font.init()

from Wall import Wall
from Powerup_OPF import PowerUp_OtherPlayerFreeze
from Powerup_SS import ShootingSpeed




class Level:
    def __init__(self, surface: pygame.Surface, level_num: int = 1) -> None:
        self.surface = surface
        self.walls = []
        self.OtherFreeze = []
        self.ShooterSpeed = []
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
                Wall(self.surface, 0.5 * screen_width, screen_height / 3.85, 30, 160)
            )
            
            self.walls.append(
                Wall(self.surface, 0.5 * screen_width, screen_height / 1.28, 30, 160)
            )

            from Powerup_OPF import PowerUp_OtherPlayerFreeze
            self.OtherFreeze.append(
                PowerUp_OtherPlayerFreeze(self.surface, 0.3 * screen_width, screen_height / 3, 20, 100)
            )
            self.OtherFreeze.append(
                PowerUp_OtherPlayerFreeze(self.surface, 0.7 * screen_width, screen_height / 3, 20, 100)
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

                self.ShooterSpeed.append(
                    ShootingSpeed(self.surface, 0.3 * screen_width, screen_height / 3, 20, 100)
                )
                self.ShooterSpeed.append(
                    ShootingSpeed(self.surface, 0.7 * screen_width, screen_height / 3, 20, 100)
                )

    def add_wall(self, wall: "Wall") -> None:
        self.walls.append(wall)

    def get_walls(self) -> list:
        return self.walls
    
    def add_otherFreeze(self, otherFreeze: "PowerUp_OtherPlayerFreeze") -> None:
        self.OtherFreeze.append(otherFreeze)
    
    def get_otherplayerfreeze(self) -> list:
        return self.OtherFreeze
    
    def add_shooterSpeed(self, shooterSpeed: "ShootingSpeed") -> None:
        self.ShooterSpeed.append(shooterSpeed)

    def get_shootingspeed(self) -> list:
        return self.ShooterSpeed
