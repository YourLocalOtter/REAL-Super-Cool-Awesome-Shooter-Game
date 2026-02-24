import sys
import random

import pygame
import pygame.locals

pygame.init()
pygame.font.init()

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
            self.walls.append(Wall(self.surface, 0.25 * screen_width, screen_height / 2, 30, 130))
            self.walls.append(Wall(self.surface, 0.75 * screen_width, screen_height / 2, 30, 130))
        elif level_num == 2:
            self.walls.append(Wall(self.surface, 0.5 * screen_width, screen_height / 3.8, 30, 160))
            self.walls.append(Wall(self.surface, 0.5 * screen_width, screen_height / 1.28, 30, 160))
        elif level_num == 3:
            for i in range(1, 4):
                self.walls.append(Wall(self.surface, 0.25 * screen_width * i, screen_height / 2, 30, 100))

    def add_wall(self, wall: 'Wall') -> None:
        self.walls.append(wall)

    def get_walls(self) -> list:
        return self.walls

class Bullets:

    def __init__(self, surface: pygame.Surface, x: float, y: float, vx: float, vy: float) -> None:
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = 5

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            int(self.radius * 2),
            int(self.radius * 2),
        )

    def teleport_offscreen(self) -> None:
        self.x = -1000
        self.y = -1000

    def update(self, walls: list['Wall']) -> bool:
        self.x += self.vx
        self.y += self.vy

        brect = self.get_rect()
        for wall in walls:
            if brect.colliderect(wall.get_rect()):
                self.teleport_offscreen()
                return False

        if (self.x - self.radius < 0 or self.x + self.radius > self.surface.get_width() or
            self.y - self.radius < 0 or self.y + self.radius > self.surface.get_height()):
            return False

        return True

    def display(self) -> None:
        pygame.draw.circle(self.surface, "#ffffff", (int(self.x), int(self.y)), self.radius)

    def check_collision(self, shooter: 'Shooters') -> bool:
        if (self.x - self.radius < shooter.x + shooter.width / 2 and
            self.x + self.radius > shooter.x - shooter.width / 2 and
            self.y - self.radius < shooter.y + shooter.height / 2 and
            self.y + self.radius > shooter.y - shooter.height / 2):
            return True
        return False

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
            bullet_vy = 0.1
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

class Wall:
    
    def __init__(self, surface: pygame.Surface, x: float, y: float, width: float, height: float) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.width, self.height = width, height

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(
            int(self.x - self.width / 2),
            int(self.y - self.height / 2),
            int(self.width),
            int(self.height),
        )

    def update(self) -> None:
        return None

    def display(self) -> None:
        r = self.get_rect()
        pygame.draw.rect(self.surface, "#964B00", r)

<<<<<<< HEAD:Main_WorkingON/2.(R)Main.py
=======
class Level:
    ...
#     class Level1:
#         ...
    
#     class Level2:
#         ...

#     class Level3:
#         ...
    

>>>>>>> 16f1c3f3ec2c6d077ad8bc690cbadc17c67eed47:copyofmainfortesting/copymain
def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    
    screen_width = random.randint(700, 1000)
    screen_height = random.randint(500, 700)
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    font = pygame.font.Font(None, 48)
    left_score = 0
    right_score = 0
    
    p_left = Shooters(
        screen,
        0.85 * screen.get_width(),
        screen.get_height() / 2,
        50,
        50,
        pygame.K_w,
        pygame.K_s,
        pygame.K_a,
        pygame.K_d,
        pygame.K_1,
        "#fbcc4a",
    )
    p_right = Shooters(
        screen,
        0.1 * screen.get_width(),
        screen.get_height() / 2,
        50,
        50,
        pygame.K_UP,
        pygame.K_DOWN,
        pygame.K_LEFT,
        pygame.K_RIGHT,
        pygame.K_RETURN,
        "#8d4fd3",
    )

<<<<<<< HEAD:Main_WorkingON/2.(R)Main.py
=======
    
>>>>>>> 16f1c3f3ec2c6d077ad8bc690cbadc17c67eed47:copyofmainfortesting/copymain
    wall = Wall(
        screen,
        0.25 * screen.get_width(),
        screen.get_height() / 2,
        30,
        130,

    )

    wall2 = Wall(
        screen,
        0.75 * screen.get_width(),
        screen.get_height() / 2,
        30,
        130,
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

    walls = [wall, wall2, wall3, wall4]
    
    while True:
        screen.fill("#82E1FE")
        
        keys_held = pygame.key.get_pressed()
        if keys_held[p_left.key_shoot]:
            p_left.shoot(-1)
        if keys_held[p_right.key_shoot]:
            p_right.shoot(1)
        
        p_left.update(walls)
        p_right.update(walls)
        p_left.display()
        p_right.display()

        
        for bullet in p_left.bullets[:]:
            if bullet.check_collision(p_right):
                right_score += 1
                p_left.bullets.remove(bullet)
        
        for bullet in p_right.bullets[:]:
            if bullet.check_collision(p_left):
                left_score += 1
                p_right.bullets.remove(bullet)
        
        if left_score >= 10 or right_score >= 10:
            winner = "Left Player" if left_score >= 10 else "Right Player"
            font_large = pygame.font.Font(None, 72)
            win_text = font_large.render(f"{winner} Wins!", True, "#ffffff")
            screen.blit(win_text, (screen.get_width() / 2 - 200, screen.get_height() / 2 - 50))
            pygame.display.flip()
            pygame.time.wait(3000)
            
            #here once someone wins, import level 2

            pygame.quit()
            sys.exit()
        
        right_score_image = font.render(f"{right_score}", True, "#ffffff")
        left_score_image = font.render(f"{left_score}", True, "#ffffff")
        screen.blit(
            left_score_image, (0.2 * screen.get_width(), 0.1 * screen.get_height())
        )
        screen.blit(
            right_score_image, (0.8 * screen.get_width(), 0.1 * screen.get_height())
        )

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
