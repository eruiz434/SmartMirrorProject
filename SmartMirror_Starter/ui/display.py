import pygame
import sys
from ui.widgets.clock_widget import draw_clock
from ui.widgets.calendar_widget import draw_calendar
from ui.widgets.weather_widget import draw_weather

def start_display():
    pygame.init()
    infoObject = pygame.display.Info()

    # Get screen size dynamically
    screen_width, screen_height = infoObject.current_w, infoObject.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    pygame.display.set_caption("SFSU Smart Mirror")

    # ✏️ Font sizes
    title_font = pygame.font.SysFont(None, 80)    # title text
    main_font = pygame.font.SysFont(None, 72)     # larger font for clock/date/weather

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # black background

        # --- Draw Header ---
        title_text = title_font.render("SFSU Smart Mirror", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, 90))
        screen.blit(title_text, title_rect)

        # --- Draw main widgets onto a temporary surface ---
        temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        draw_clock(temp_surface, main_font)
        draw_calendar(temp_surface, main_font)
        draw_weather(temp_surface, main_font)

        # --- Find bounding box for all widgets ---
        temp_rect = temp_surface.get_bounding_rect()

        # --- Compute centered position slightly lower than title ---
        centered_x = (screen_width - temp_rect.width) // 2
        centered_y = (screen_height - temp_rect.height) // 2 + 60  # move down a little below title

        screen.blit(temp_surface, (centered_x - temp_rect.x, centered_y - temp_rect.y))

        pygame.display.flip()
