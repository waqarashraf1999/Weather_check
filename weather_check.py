import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
        else:
            print(f"Failed to get weather information. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = "YOUR_API_KEY"
city_name = input("Enter the city name: ")

get_weather(api_key, city_name)
