import sys
import random

import pygame
import pygame.locals

pygame.init()
pygame.font.init()

from Bullets.Bulleitos import Bullets
from Walls.Wall import Wall


class Shooters:

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
            key_shoot: int,
            color: str,
        ) -> None:
            self.surface = surface
            self.x, self.y = x, y
            self.width, self.height = width, height
            self.key_up = key_up
            self.key_down = key_down
            self.key_left = key_left
            self.key_right = key_right
            self.key_shoot = key_shoot
            self.vx = 0
            self.vy = 0
            self.speed = 5
            self.bullets = []
            self.max_bullets = 1
            self.color = color


        def shoot(self, direction: int) -> None:
            if len(self.bullets) < self.max_bullets:
                bullet_vx = 10 * direction
                bullet_vy = 0
                bullet = Bullets(self.surface, self.x, self.y, bullet_vx, bullet_vy)
                self.bullets.append(bullet)
        
        def get_rect(self) -> pygame.Rect:
            return pygame.Rect(
                int(self.x - self.width / 2),
                int(self.y - self.height / 2),
                int(self.width),
                int(self.height),
            )

        def update(self, walls: list['Wall']) -> None:
            keys_held = pygame.key.get_pressed()
            self.vx = self.speed * (keys_held[self.key_right] - keys_held[self.key_left])
            self.vy = self.speed * (keys_held[self.key_down] - keys_held[self.key_up])
            rect = self.get_rect()
            rect.x += int(self.vx)

            if rect.left < 0:
                rect.left = 0
            if rect.right > self.surface.get_width():
                rect.right = self.surface.get_width()

            for wall in walls:
                wrect = wall.get_rect()
                if rect.colliderect(wrect):
                    if self.vx > 0:
                        rect.right = wrect.left
                    elif self.vx < 0:
                        rect.left = wrect.right

            rect.y += int(self.vy)

            if rect.top < 0:
                rect.top = 0
            if rect.bottom > self.surface.get_height():
                rect.bottom = self.surface.get_height()

            for wall in walls:
                wrect = wall.get_rect()
                if rect.colliderect(wrect):
                    if self.vy > 0:
                        rect.bottom = wrect.top
                    elif self.vy < 0:
                        rect.top = wrect.bottom

            self.x = rect.centerx
            self.y = rect.centery

            for bullet in self.bullets[:]:
                if not bullet.update(walls):
                    self.bullets.remove(bullet)

        def display(self) -> None:
            rect_x = self.x - self.width / 2
            rect_y = self.y - self.height / 2
            pygame.draw.rect(self.surface, self.color, (rect_x, rect_y, self.width, self.height))
            
            for bullet in self.bullets:
                bullet.display()