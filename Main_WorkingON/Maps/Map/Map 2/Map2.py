import sys

import pygame
import pygame.locals

from Items2 import Wall2
from Items2 import PowerUp_ShootSpeed


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))

    wall = Wall2(
        screen,
        0.25 * screen.get_width(),
        screen.get_height() / 1.2,
        30,
        160,

    )


    wall2 = Wall2(
        screen,
        0.40 * screen.get_width(), #place on screen on the x value
        screen.get_height() / 1.2,
        30,
        160,
#y position, width, length
    )

    wall3 = Wall2(
        screen,
        0.60 * screen.get_width(),
        screen.get_height() / 5,
        30,
        160,

    )


    wall4 = Wall2(
        screen,
        0.75 * screen.get_width(),
        screen.get_height() / 5,
        30,
        160,

    )

    shootspeed = PowerUp_ShootSpeed(
        screen,
        0.34 * screen.get_width(),
        screen.get_height() / 1.05,
        30,
        160,
    )

    shootspeed2 = PowerUp_ShootSpeed(
        screen,
        0.69 * screen.get_width(),
        screen.get_height() / 3.12,
        30,
        160,
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
        wall4.update()
        wall4.display()
        shootspeed.update()
        shootspeed.display()
        shootspeed2.update()
        shootspeed2.display()

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()