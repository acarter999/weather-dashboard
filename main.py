import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        print("Could not retrieve weather data.")
        return

    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    print(f"\nWeather for {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {description.capitalize()}")


def main():
    city = input("Enter a city name: ").strip()

    if not city:
        print("Please enter a valid city.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
