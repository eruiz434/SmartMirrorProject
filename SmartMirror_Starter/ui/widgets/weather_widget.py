import pygame
import requests
from io import BytesIO
from PIL import Image

# 🗝️ Your API key from OpenWeatherMap
API_KEY = "8eeaea677d2dbfc9d1b4ca8c0afbf6d4"
CITY = "San Francisco"   # change to your city
UNITS = "imperial"       # use "metric" for °C

def get_weather():
    """Fetch current weather data from OpenWeatherMap."""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = int(data["main"]["temp"])
            description = data["weather"][0]["description"].title()
            icon_code = data["weather"][0]["icon"]
            return f"{description}, {temp}°F", icon_code
        else:
            print("Weather error:", data)
            return "Weather Unavailable", "01d"
    except Exception as e:
        print("Error fetching weather:", e)
        return "Error", "01d"


def draw_weather(screen, font):
    """Draw live weather text and icon."""
    weather_str, icon_code = get_weather()

    # --- Download and prepare the icon ---
    try:
        url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(url)
        image_data = BytesIO(response.content)

        pil_image = Image.open(image_data).convert("RGBA")
        pil_image = pil_image.resize((50, 50))  # smaller icon
        mode = pil_image.mode
        size = pil_image.size
        data = pil_image.tobytes()

        icon_surface = pygame.image.fromstring(data, size, mode)
        screen.blit(icon_surface, (10, 140))
    except Exception as e:
        print("Icon error:", e)

    # --- Draw weather text ---
    text = font.render(weather_str, True, (255, 255, 255))
    screen.blit(text, (70, 155))
