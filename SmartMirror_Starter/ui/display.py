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

    pygame.display.set_caption("Smart Mirror")
    font = pygame.font.SysFont(None, 48)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # black background

        screen_width, screen_height = screen.get_size()

        # Create a surface where widgets are drawn
        temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        # Draw widgets as usual
        draw_clock(temp_surface, font)
        draw_calendar(temp_surface, font)
        draw_weather(temp_surface, font)

        # --- Calculate bounding box of all non-black pixels ---
        temp_rect = temp_surface.get_bounding_rect()

        # --- Compute exact centered position ---
        centered_x = (screen_width - temp_rect.width) // 2
        centered_y = (screen_height - temp_rect.height) // 2

        # --- Blit the content block centered on screen ---
        screen.blit(temp_surface, (centered_x - temp_rect.x, centered_y - temp_rect.y))

        pygame.display.flip()
