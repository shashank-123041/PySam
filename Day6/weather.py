import requests

api_key = "9b9a261ebeec52f04f3ce4e0839afff8"
city = 'Antarctica'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
print(url)
if response.status_code == 200:
    weather_data = response.json()
    print()
    print(f"City: {weather_data['name']}")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    print()
else:
    print(f"Failed to get weather data. Status code: {response.status_code}")
