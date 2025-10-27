import pygame
import sys
from ui.widgets.clock_widget import draw_clock
from ui.widgets.calendar_widget import draw_calendar
from ui.widgets.weather_widget import draw_weather

def start_display():
    pygame.init()
    infoObject = pygame.display.Info()

    # Make sure we match your display size dynamically
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

        # 🪞 Create a surface for all widgets together
        mirror_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        # Draw widgets onto the mirror surface
        draw_clock(mirror_surface, font)
        draw_calendar(mirror_surface, font)
        draw_weather(mirror_surface, font)

        # 🧭 Center the entire mirror content
        mirror_rect = mirror_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(mirror_surface, mirror_rect)

        pygame.display.flip()
