import pygame

def draw_weather(screen, font):
    # Example: Hardcoded weather, you can connect API later
    weather_str = "Sunny, 72°F"
    text = font.render(weather_str, True, (255, 255, 255))
    screen.blit(text, (50, 170))