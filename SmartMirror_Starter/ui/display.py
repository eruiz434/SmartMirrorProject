import pygame
import sys
from ui.widgets.clock_widget import draw_clock
from ui.widgets.calendar_widget import draw_calendar
from ui.widgets.weather_widget import draw_weather

def start_display():
    pygame.init()
    infoObject = pygame.display.Info()

    screen_width, screen_height = infoObject.current_w, infoObject.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("SFSU Smart Mirror")

    # Fonts
    title_font = pygame.font.SysFont(None, 80)
    main_font = pygame.font.SysFont(None, 72)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        # --- Draw header a little higher ---
        title_text = title_font.render("SFSU Smart Mirror", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 4.7))
        screen.blit(title_text, title_rect)

        # --- Draw widgets onto a temp surface ---
        temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        draw_clock(temp_surface, main_font)
        draw_calendar(temp_surface, main_font)
        draw_weather(temp_surface, main_font)

        # Bounding box for widgets
        content_rect = temp_surface.get_bounding_rect()

        # Center all widgets together below the title
        group_y = title_rect.bottom + 300  # space under the title
        centered_x = (screen_width - content_rect.width) // 2
        screen.blit(
            temp_surface,
            (centered_x - content_rect.x, group_y - content_rect.y)
        )

        pygame.display.flip()
