import sys
import random

import pygame
import pygame.locals

pygame.init()
pygame.font.init()



class Bullets:
    def __init__(self, surface: pygame.Surface, x: float, y: float, vx: float, vy: float) -> None:
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = 5

    def update(self) -> bool:
        self.x += self.vx
        self.y += self.vy
        
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

    def update(self) -> None:
        keys_held = pygame.key.get_pressed()
        self.vx = self.speed * (keys_held[self.key_right] - keys_held[self.key_left])
        self.vy = self.speed * (keys_held[self.key_down] - keys_held[self.key_up])
        
        self.x += self.vx
        self.y += self.vy
        
        if self.x < self.width/2:
            self.x = self.width/2
        if self.x > self.surface.get_width() - self.width/2:
            self.x = self.surface.get_width() - self.width/2
        if self.y < self.height/2:
            self.y = self.height/2
        if self.y > self.surface.get_height() - self.height/2:
            self.y = self.surface.get_height() - self.height/2
        
        for bullet in self.bullets[:]:
            if not bullet.update():
                self.bullets.remove(bullet)

    def display(self) -> None:
        rect_x = self.x - self.width / 2
        rect_y = self.y - self.height / 2
        pygame.draw.rect(self.surface, self.color, (rect_x, rect_y, self.width, self.height))
        
        for bullet in self.bullets:
            bullet.display()


class Wall:

    def __init__(
        self,
        surface: pygame.Surface,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.width, self.height = width, height


    def update(self) -> None:
        return None

    def display(self) -> None:
        rect_x = self.x - self.width / 2
        rect_y = self.y - self.height / 2
        pygame.draw.rect(self.surface, "#964B00", (rect_x, rect_y, self.width, self.height))

<<<<<<< HEAD:Main_WorkingON/2.(R)Main.py
<<<<<<< HEAD:copyofmainfortesting/copymain
class Wall2:

    def __init__(
        self,
        surface: pygame.Surface,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.width, self.height = width, height


    def update(self) -> None:
        return None

    def display(self) -> None:
        rect_x = self.x - self.width / 2
        rect_y = self.y - self.height / 2
        pygame.draw.rect(self.surface, "#964B00", (rect_x, rect_y, self.width, self.height))

class PowerUp_ShootSpeed:

    def __init__(
        self,
        surface: pygame.Surface,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.width, self.height = width, height

    def update(self) -> None:
        return None
    
    def display(self) -> None:
        rect_x = self.x - self.width / 2
        rect_y = self.y - self.height / 2
        pygame.draw.circle(self.surface, "#FF21EA", (rect_x,rect_y), 20, width=0)

class Game:
=======
<<<<<<< HEAD:Main_WorkingON/2.(R)Main.py
=======
class Level:
>>>>>>> 05f2bee0d736acb9b49bfaf2e471aebb408cd5ba:Main_WorkingON/2.(R)Main.py
    ...
#     class Level1:
#         ...
    
#     class Level2:
#         ...
=======
>>>>>>> 05d385c37323a8ab484e6a885fe4b0485e5f5442:Archieves/1.Main.py

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    
    screen_width = 1000
    screen_height = 700
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
    
    state = "start"


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
        screen.fill("#82E1FE")
        
        keys_held = pygame.key.get_pressed()
        if keys_held[p_left.key_shoot]:
            p_left.shoot(-1)
        if keys_held[p_right.key_shoot]:
            p_right.shoot(1)
        
        p_left.update()
        p_left.display()
        p_right.update()
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
<<<<<<< HEAD:Main_WorkingON/2.(R)Main.py

            #here once someone wins, import level 2
            # if winner == True:
            #     wall = Wall2
            #     wall2 = Wall2
            #     wall3 = Wall2
            #     wall4 = Wall2


=======
>>>>>>> 05d385c37323a8ab484e6a885fe4b0485e5f5442:Archieves/1.Main.py
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
        
        # if state == "start":
        #     screen.fill("#00BE49")
        # elif state == "game":
        #     screen.fill("#5FDBF7")
        # elif state == "dead":
        #     screen.fill("#330000")
        
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if state == "start":
                        state = "game"
                    elif state == "game":
                        state = "game"
                if event.key == pygame.K_r:
                    if state == "dead":
                        state = "start"

            # elif event.type == pygame.locals.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         if state == "start":
            #             state = "game"
            #         elif state == "game":
            #             state = "game"
            #     if event.key == pygame.K_r:
            #         if state == "dead":
            #             state = "start"
                

        wall.update()
        wall.display()
        wall2.update()
        wall2.display()
        wall3.update()
        wall3.display()
        wall4.update()
        wall4.display()
<<<<<<< HEAD:Main_WorkingON/2.(R)Main.py
    
=======
>>>>>>> 05d385c37323a8ab484e6a885fe4b0485e5f5442:Archieves/1.Main.py

        pygame.display.flip()
        fps_clock.tick(fps)

if __name__ == "__main__":
    main()

