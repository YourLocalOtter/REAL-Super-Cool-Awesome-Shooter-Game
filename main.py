import sys
import random

import pygame
import pygame.locals

from shooter import Shooter
from level import Level

Leval = 0

def main():

    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    
    screen_width = random.randint(700, 1000)
    screen_height = random.randint(500, 700)
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    background_image = pygame.image.load("background.jpg")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    
    font = pygame.font.Font(None, 48)
    left_score = 0
    right_score = 0

    current_level = 1
    level = Level(screen, current_level)
    walls = level.get_walls()
    
    p_left = Shooter(
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
    p_right = Shooter(
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

    while True:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.blit(background_image, (0, 0))

        
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
            if bullet.check_collision(p_right.x, p_right.y, p_right.width, p_right.height):
                right_score += 1
                p_left.bullets.remove(bullet)
        
        for bullet in p_right.bullets[:]:
            if bullet.check_collision(p_left.x, p_left.y, p_left.width, p_left.height):
                left_score += 1
                p_right.bullets.remove(bullet)
        
        if left_score >= 5 or right_score >= 5:
            current_level += 1
            if current_level > 3:
                    winner = "Left Player" if left_score > right_score else "Right Player"
                    font_large = pygame.font.Font(None, 72)
                    win_text = font_large.render(f"{winner} Wins!", True, "#ffffff")
                    screen.blit(win_text, (screen.get_width() / 2 - 200, screen.get_height() / 2 - 50))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    pygame.quit()
                    sys.exit()
            level = Level(screen, current_level)
            walls = level.get_walls()
    
            left_score = 0
            right_score = 0
        
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

        for wall in walls:
            wall.update()
            wall.display()

        pygame.display.flip()
        fps_clock.tick(fps)
        
if __name__ == "__main__":
    main()