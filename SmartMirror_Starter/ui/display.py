import pygame
import sys
from ui.widgets.clock_widget import draw_clock
from ui.widgets.calendar_widget import draw_calendar
from ui.widgets.weather_widget import draw_weather

def start_display():
    pygame.init()
    infoObject = pygame.display.Info()

    # Match screen size dynamically
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
        center_x = screen_width // 2

        # --- Clock ---
        clock_surface = pygame.Surface((screen_width, 100), pygame.SRCALPHA)
        draw_clock(clock_surface, font)
        clock_rect = clock_surface.get_rect(center=(center_x, screen_height // 2 - 120))
        screen.blit(clock_surface, clock_rect)

        # --- Calendar ---
        calendar_surface = pygame.Surface((screen_width, 100), pygame.SRCALPHA)
        draw_calendar(calendar_surface, font)
        calendar_rect = calendar_surface.get_rect(center=(center_x, screen_height // 2 - 50))
        screen.blit(calendar_surface, calendar_rect)

        # --- Weather ---
        wea
