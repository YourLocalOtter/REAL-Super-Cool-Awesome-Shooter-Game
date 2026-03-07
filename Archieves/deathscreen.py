import pygame

class DeathScreen:
    def __init__(self, screen_width=800, screen_height=600):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font_large = pygame.font.Font(None, 80)
        self.font_small = pygame.font.Font(None, 40)
        self.show = False

    def display(self, screen):
        if not self.show:
            return

        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        death_text = self.font_large.render("YOU'RE DEAD", True, (255, 0, 0))
        death_rect = death_text.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2 - 80)
        )
        screen.blit(death_text, death_rect)

        round_text = self.font_small.render(
            "Press SPACE for New Round", True, (255, 255, 255)
        )
        round_rect = round_text.get_rect(
            center=(self.screen_width // 2, self.screen_height // 2 + 80)
        )
        screen.blit(round_text, round_rect)

    def check_death(self, hit_count, max_hits=5):
        """Check if player is dead based on hit count"""
        if hit_count >= max_hits:
            self.show = True

    def reset(self):
        """Reset death screen for new round"""
        self.show = False
