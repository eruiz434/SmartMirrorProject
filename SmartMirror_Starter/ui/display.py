import pygame
import sys
from ui.widgets.clock_widget import draw_clock
from ui.widgets.calendar_widget import draw_calendar
from ui.widgets.weather_widget import draw_weather

def start_display():
    pygame.init()
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((1080, 1920), pygame.FULLSCREEN)


    pygame.display.set_caption("Smart Mirror")
    font = pygame.font.SysFont(None, 48)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        draw_clock(screen, font)
        draw_calendar(screen, font)
        draw_weather(screen, font)
        pygame.display.flip()