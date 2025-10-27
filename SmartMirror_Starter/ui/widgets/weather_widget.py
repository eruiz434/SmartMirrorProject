import pygame
import requests
from io import BytesIO
from PIL import Image

def draw_weather(screen, font):
    # Example weather info (replace this later with live API data)
    weather_str = "Sunny, 72°F"
    icon_code = "01d"  # 01d = clear day icon from OpenWeatherMap

    # --- Load weather icon from OpenWeatherMap ---
    try:
        url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(url)
        image_data = BytesIO(response.content)

        # Convert image to Pygame surface
        pil_image = Image.open(image_data).convert("RGBA")
        pil_image = pil_image.resize((50, 50))  # smaller icon
        mode = pil_image.mode
        size = pil_image.size
        data = pil_image.tobytes()

        icon_surface = pygame.image.fromstring(data, size, mode)

        # Draw the icon
        screen.blit(icon_surface, (10, 140))  # position on mirror
    except Exception as e:
        print(f"Weather icon failed to load: {e}")

    # --- Draw weather text ---
    text = font.render(weather_str, True, (255, 255, 255))
    screen.blit(text, (70, 155))  # next to icon
