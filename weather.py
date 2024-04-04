import requests

def get_weather(api_key, location):
    """
    Fetch current weather data for a specified location using OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    """
    Display basic weather information such as temperature, humidity, and weather conditions.
    """
    if weather_data["cod"] == 200:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_condition = weather_data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("Error: Unable to fetch weather data. Please check your input.")
def main():
    print("Welcome to the Command Line Weather App!")
    api_key ="3e0e264c9728760c8fbd9ceea912b41c"
    location = input("Enter the location (city name or ZIP code): ")

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
