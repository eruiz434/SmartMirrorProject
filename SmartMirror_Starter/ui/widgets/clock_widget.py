import datetime
import pygame

def draw_clock(screen, font):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    text = font.render(now, True, (255, 255, 255))
    screen.blit(text, (50, 30))