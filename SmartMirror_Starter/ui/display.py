import pygame
import sys
from ui.widgets.clock_widget import draw_clock
from ui.widgets.calendar_widget import draw_calendar
from ui.widgets.weather_widget import draw_weather

def start_display():
    pygame.init()
    infoObject = pygame.display.Info()

    # Get your screen size dynamically
    screen_width, screen_height = infoObject.current_w, infoObject.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    pygame.display.set_caption("Smart Mirror")
    font = pygame.font.SysFont(None, 48)

    # Center offset controls (change these values to fine-tune placement)
    x_offset = screen_width // 4      # centers horizontally
    y_offset = screen_height // 4     # centers vertically

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # black background

        # Move entire layout down/right from the top-left corner
        mirror_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        mirror_surface.blit(screen, (0, 0))

        # Apply the offset to all widget drawings
        temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        draw_clock(temp_surface, font)
        draw_calendar(temp_surface, font)
        draw_weather(temp_surface, font)

        # Blit everything shifted to the center area
        screen.blit(temp_surface, (x_offset, y_offset))

        pygame.display.flip()
