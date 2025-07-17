import requests


# Your API key
api_key = "5dd4ca87f875489f5e17ad20f28834c3"

# Ask user for city
city = input("Enter city name: ")

# URL for OpenWeatherMap API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Sending GET request
response = requests.get(url)

# Convert JSON response to dictionary
data = response.json()

# Check if city is found
if data["cod"] == 200:
    main = data["main"]
    wind = data["wind"]
    weather = data["weather"][0]

    print(f"\nWeather in {city.capitalize()}:")
    print(f"Temperature: {main['temp']}°C")
    print(f"Description: {weather['description'].capitalize()}")
    print(f"Humidity: {main['humidity']}%")
    print(f"Wind Speed: {wind['speed']} m/s")
else:
    print("City not found. Please check the spelling.")
