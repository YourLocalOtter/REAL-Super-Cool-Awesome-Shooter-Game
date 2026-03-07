import sys

import pygame
import pygame.locals

from Wall import Wall
from Powerup_SS import ShootingSpeed
from Powerup_OPF import PowerUp_OtherPlayerFreeze


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))

    wall = Wall(
        screen,
        0.75 * screen.get_width(),
        screen.get_height() / 1.2,
        30,
<<<<<<< HEAD
        130,
=======
        160,

>>>>>>> c8e05a2a55d708a95857d675440df292480e17bc
    )

    wall2 = Wall(
        screen,
<<<<<<< HEAD
        0.75 * screen.get_width(),  # place on screen on the x value
        screen.get_height() / 2,
        30,
        130,
        # y position, width, length
=======
        0.50 * screen.get_width(), #place on screen on the x value
        screen.get_height() / 2.0,
        30,
        160,
#y position, width, length
>>>>>>> c8e05a2a55d708a95857d675440df292480e17bc
    )

    wall3 = Wall(
        screen,
        0.25 * screen.get_width(),
        screen.get_height() / 5,
        30,
        160,
    )

<<<<<<< HEAD
    wall4 = Wall(
=======
    otherplayerfreeze = PowerUp_OtherPlayerFreeze(
>>>>>>> c8e05a2a55d708a95857d675440df292480e17bc
        screen,
        0.3 * screen.get_width(),
        screen.get_height() / 1,
        30,
        160,
<<<<<<< HEAD
=======
    )

    otherplayerfreeze2 = PowerUp_OtherPlayerFreeze(
        screen,
        0.80 * screen.get_width(),
        screen.get_height() / 4,
        30,
        160,
    )



    shootingspeed = ShootingSpeed(
        screen,
        0.3 * screen.get_width(),
        screen.get_height() / 1,
        30,
        160,
    )

    shootingspeed2 = ShootingSpeed(
        screen,
        0.80 * screen.get_width(),
        screen.get_height() / 4,
        30,
        160,
>>>>>>> c8e05a2a55d708a95857d675440df292480e17bc
    )

    while True:
        screen.fill("#000000")

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        wall.update()
        wall.display()
        wall2.update()
        wall2.display()
        wall3.update()
        wall3.display()
        otherplayerfreeze.update()
        otherplayerfreeze.display()
        otherplayerfreeze2.update()
        otherplayerfreeze2.display()
        shootingspeed.update()
        shootingspeed.display()
        shootingspeed2.update()
        shootingspeed2.display()

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
