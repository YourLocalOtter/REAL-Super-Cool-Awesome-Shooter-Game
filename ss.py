import pygame
import sys


def start_screen():

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("SMBH.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

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
    mute_button_width = 100
    mute_button_height = 50
    mute_button_rect = pygame.Rect(
        10,
        screen_height - mute_button_height - 10,
        mute_button_width,
        mute_button_height,
    )
    is_muted = False

    background_image = pygame.image.load("sunset.png")
    background_image = pygame.transform.scale(
        background_image, (screen_width, screen_height)
    )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False
                    from main import main

                    main()
                if rules_button_rect.collidepoint(event.pos):
                    show_rules = not show_rules
                if mute_button_rect.collidepoint(event.pos):
                    is_muted = not is_muted
                    if is_muted:
                        pygame.mixer.music.set_volume(0)
                    else:
                        pygame.mixer.music.set_volume(0.05)

        screen.blit(background_image, (0, 0))

        if not show_rules:
            title = font_large.render(
                "SUPER COOL & AWESOME SHOOTER GAME", True, "#ffe7ae"
            )
            pygame.draw.rect(screen, "#ff7746", (20, 135, 760, 50), border_radius=8)
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
                "First to hit opponent 10 times wins",
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

        mute_button_color = (
            "#ff7746" if mute_button_rect.collidepoint(mouse_pos) else "#80f4ec"
        )
        pygame.draw.rect(screen, mute_button_color, mute_button_rect, border_radius=10)
        mute_text = font_small.render(
            "MUTE" if not is_muted else "UNMUTE", True, "#ffffff"
        )
        mute_text_rect = mute_text.get_rect(center=mute_button_rect.center)
        screen.blit(mute_text, mute_text_rect)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    start_screen()
