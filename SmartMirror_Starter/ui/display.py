import pygame
import sys
from ui.widgets.clock_widget import draw_clock
from ui.widgets.calendar_widget import draw_calendar
from ui.widgets.weather_widget import draw_weather

def start_display():
    pygame.init()
    infoObject = pygame.display.Info()

    # Match your display resolution (portrait)
    screen_width, screen_height = infoObject.current_w, infoObject.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    pygame.display.set_caption("Smart Mirror")
    font = pygame.font.SysFont(None, 48)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Black background

        # 🪞 Create a container surface for all widgets
        mirror_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        # Draw widgets as usual on the mirror surface
        draw_clock(mirror_surface, font)
        draw_calendar(mirror_surface, font)
        draw_weather(mirror_surface, font)

        # 🧭 Calculate offsets to center the entire layout
        layout_rect = mirror_surface.get_rect()
        offset_x = (screen_width - layout_rect.width) // 2
        offset_y = (screen_height - layout_rect.height) // 2

        # Blit the mirror surface centered on the screen
        screen.blit(mirror_surface, (offset_x, offset_y))

        pygame.display.flip()
