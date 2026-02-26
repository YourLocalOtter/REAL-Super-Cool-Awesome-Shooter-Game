import sys

import pygame
import pygame.locals

from items import Wall


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))

    wall = Wall(
        screen,
        0.25 * screen.get_width(),
        screen.get_height() / 2,
        30,
        130,

    )


    wall2 = Wall(
        screen,
        0.75 * screen.get_width(), #place on screen on the x value
        screen.get_height() / 2,
        30,
        130,
#y position, width, length
    )

    wall3 = Wall(
        screen,
        0.50 * screen.get_width(),
        screen.get_height() / 3.8,
        30,
        160,

    )


    wall4 = Wall(
        screen,
        0.50 * screen.get_width(),
        screen.get_height() / 1.28,
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

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()