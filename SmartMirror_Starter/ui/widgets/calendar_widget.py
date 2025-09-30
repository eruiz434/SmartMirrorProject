import datetime
import pygame

def draw_calendar(screen, font):
    today = datetime.date.today()
    date_str = today.strftime("%A, %B %d, %Y")
    text = font.render(date_str, True, (255, 255, 255))
    screen.blit(text, (50, 100))