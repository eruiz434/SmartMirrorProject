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
    title_font = pygame.font.SysFont(None, 80)   # big header
    main_font = pygame.font.SysFont(None, 56)    # larger for clock/date/weather

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # black background

        # Draw header text
        title_text = title_font.render("SFSU Smart Mirror", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, 80))
        screen.blit(title_text, title_rect)

        # Create a surface for all widgets
        temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        # Draw widgets
        draw_clock(temp_surface, main_font)
        draw_calendar(temp_surface, main_font)
        draw_weather(temp_surface, main_font)

        # Get bounding box for all drawn content
        temp_rect = temp_surface.get_bounding_rect()

        # Compute centered position
        centered_x = (screen_width - temp_rect.width) // 2
        centered_y = (screen_height - temp_rect.height) // 2 + 40  # shifted slightly down

        # Draw the widget block centered on screen
        screen.blit(temp_surface, (centered_x - temp_rect.x, centered_y - temp_rect.y))

        pygame.display.flip()
