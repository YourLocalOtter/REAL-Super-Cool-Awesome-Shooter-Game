import sys

import pygame
import pygame.locals

class Player:

    def __init__(
        self,
        surface: pygame.Surface,
        x: float,
        y: float,
        width: float,
        height: float,
        key_up: int,
        key_down: int,
        key_left: int,
        key_right: int,

    ) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.key_left = key_left
        self.key_right = key_right
        self.key_up = key_up
        self.key_down = key_down
        self.vx = 100
        self.vy = 100

    def update(self) -> None:
        keys_held = pygame.key.get_pressed()
        self.vy += 100 * (keys_held[self.key_down] - keys_held[self.key_up])
        self.vx += 100 * (keys_held[self.key_left] - keys_held[self.key_right])
        self.vy *= 0.2
        self.vx *= 0.2
        self.y += self.vy
        self.x += self.vx
        if self.y < self.height/2:
            self.y = self.height/2
            self.vy *= -1
        if self.y > self.surface.get_height() - self.height/2:
            self.y = self.surface.get_height() - self.height/2
            self.vy *= -1
        if self.x < self.width/2:
            self.x = self.width/2
            self.vx *= -1
        if self.x > self.surface.get_width() - self.width/2:
            self.x = self.surface.get_width() - self.width/2
            self.vx *= -1

    def display(self) -> None:
        rect_x = self.x - self.width / 2
        rect_y = self.y - self.height / 2
        pygame.draw.rect(self.surface, "#ffffff", (rect_x, rect_y, self.width, self.height))


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    p_left = Player(
        screen,
        0.1 * screen.get_width(),
        screen.get_height() / 2,
        50,
        50,
        pygame.K_w,
        pygame.K_s,
        pygame.K_a,
        pygame.K_d,
    )
    p_right = Player(
        screen,
        0.9 * screen.get_width(),
        screen.get_height() / 2,
        50,
        50,
        pygame.K_UP,
        pygame.K_DOWN,
        pygame.K_LEFT,
        pygame.K_RIGHT,
    )
    
    while True:
        screen.fill("#82E1FE")
        p_left.update()
        p_left.display()
        p_right.update()
        p_right.display()

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()