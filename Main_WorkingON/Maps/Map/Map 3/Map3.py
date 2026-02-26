import sys

import pygame
import pygame.locals

from Items3 import Wall3
from Items3 import PowerUp_OtherPlayerFreeze


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))

    wall = Wall3(
        screen,
        0.75 * screen.get_width(),
        screen.get_height() / 1.2,
        30,
        160,

    )


    wall2 = Wall3(
        screen,
        0.50 * screen.get_width(), #place on screen on the x value
        screen.get_height() / 2.0,
        30,
        160,
#y position, width, length
    )

    wall3 = Wall3(
        screen,
        0.25 * screen.get_width(),
        screen.get_height() / 5,
        30,
        160,

    )


    otherplayerfreeze = PowerUp_OtherPlayerFreeze(
        screen,
        0.3 * screen.get_width(),
        screen.get_height() / 1,
        30,
        160,
    )

    otherplayerfreeze2 = PowerUp_OtherPlayerFreeze(
        screen,
        0.80 * screen.get_width(),
        screen.get_height() / 4,
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
        otherplayerfreeze.update()
        otherplayerfreeze.display()
        otherplayerfreeze2.update()
        otherplayerfreeze2.display()

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()