import pygame
import sys
from ui.widgets.clock_widget import draw_clock
from ui.widgets.calendar_widget import draw_calendar
from ui.widgets.weather_widget import draw_weather

def start_display():
    pygame.init()
    infoObject = pygame.display.Info()

    # Use your full display resolution
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

        screen.fill((0, 0, 0))  # background

        # --- Draw all elements on a temporary surface ---
        temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        # Draw widgets (clock/date/weather)
        draw_clock(temp_surface, main_font)
        draw_calendar(temp_surface, main_font)
        draw_weather(temp_surface, main_font)

        # Measure bounding box of widgets
        content_rect = temp_surface.get_bounding_rect()

        # Create a combined surface that includes the title + widgets
        full_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        # Draw title on full_surface
        title_text = title_font.render("SFSU Smart Mirror", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen_width // 2, 0))  # placeholder
        title_height = title_rect.height

        # Draw widgets below the title with spacing
        spacing = 40
        group_height = title_height + spacing + content_rect.height

        # Calculate where to start so the entire group is centered
        start_y = (screen_height - group_height) // 2

        # Title position
        title_rect.center = (screen_width // 2, start_y + title_height // 2)
        full_surface.blit(title_text, title_rect)

        # Widget block position
        widgets_y = start_y + title_height + spacing
        full_surface.blit(temp_surface, ( (screen_width - content_rect.width)//2 - content_rect.x, widgets_y - content_rect.y ))

        # Blit entire layout to screen
        screen.blit(full_surface, (0, 0))

        pygame.display.flip()
