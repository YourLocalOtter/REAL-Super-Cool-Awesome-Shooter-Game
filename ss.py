import pygame
import sys
from main import main


def start_screen():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Shooter Game")

    clock = pygame.time.Clock()
    font_large = pygame.font.Font(None, 50)
    font_medium = pygame.font.Font(None, 36)
    font_small = pygame.font.Font(None, 24)

    button_width = 200
    button_height = 60
    button_x = screen_width // 2 - button_width // 2
    button_y = screen_height // 2 + 100
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    rules_button_width = 150
    rules_button_height = 50
    rules_button_rect = pygame.Rect(
        screen_width // 2 - rules_button_width // 2,
        button_y + 80,
        rules_button_width,
        rules_button_height,
    )

    button_width = 200
    button_height = 60
    button_x = screen_width // 2 - button_width // 2
    button_y = screen_height // 2 + 100
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    rules_button_width = 100
    rules_button_height = 50
    rules_button_rect = pygame.Rect(
        screen_width - rules_button_width - 10,
        10,
        rules_button_width,
        rules_button_height,
    )

    show_rules = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pygame.quit()
                    main()
                if rules_button_rect.collidepoint(event.pos):
                    show_rules = not show_rules

        background_image = pygame.image.load("sunset.png")
        background_image = pygame.transform.scale(
            background_image, (screen_width, screen_height)
        )
        screen.blit(background_image, (0, 0))

        if not show_rules:
            title = font_large.render(
                "SUPER COOL & AWESOME SHOOTER GAME", True, "#ffe7ae"
            )
            title_rect = title.get_rect(center=(screen_width // 2, 160))
            screen.blit(title, title_rect)

            subtitle = font_medium.render("Battle your opponent!", True, "#543000")
            subtitle_rect = subtitle.get_rect(center=(screen_width // 2, 210))
            screen.blit(subtitle, subtitle_rect)

            mouse_pos = pygame.mouse.get_pos()
            button_color = (
                "#ff7746" if button_rect.collidepoint(mouse_pos) else "#673709"
            )
            pygame.draw.rect(screen, button_color, button_rect, border_radius=10)

            button_text = font_medium.render("START", True, "#ffffff")
            button_text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, button_text_rect)
        else:
            title = font_large.render("RULES", True, "#000000")
            title_rect = title.get_rect(center=(screen_width // 2, 10))
            screen.blit(title, title_rect)

            rules = [
                "Left Player: W/A/S/D to move, 1 to shoot",
                "Right Player: Arrow keys to move, Return to shoot",
                "First to hit opponent 3 times wins",
                "Unlimited bullets",
            ]

            y_offset = 150
            for rule in rules:
                rule_text = font_small.render(rule, True, "#ffffff")
                rule_rect = rule_text.get_rect(center=(screen_width // 2, y_offset))
                screen.blit(rule_text, rule_rect)
                y_offset += 60

        mouse_pos = pygame.mouse.get_pos()
        rules_button_color = (
            "#ff7746" if rules_button_rect.collidepoint(mouse_pos) else "#80f4ec"
        )
        pygame.draw.rect(
            screen, rules_button_color, rules_button_rect, border_radius=10
        )

        rules_button_text = font_small.render("RULES", True, "#ffffff")
        rules_button_text_rect = rules_button_text.get_rect(
            center=rules_button_rect.center
        )
        screen.blit(rules_button_text, rules_button_text_rect)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    start_screen()
