import requests
from bs4 import BeautifulSoup

def get_weather_data():
    # Send a GET request to the website
    response = requests.get('https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671')

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the weather data
        temperature = soup.find('span', class_='temperature').text
        humidity = soup.find('span', class_='humidity').text
        wind_speed = soup.find('span', class_='wind-speed').text

        # Return the weather data as a dictionary
        weather_data = {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }

        return weather_data

    else:
        print('Error: Failed to fetch weather data.')
        return None

if __name__ == '__main__':
    weather_data = get_weather_data()

    if weather_data:
        print('Weather Data:')
        print(f'Temperature: {weather_data["temperature"]}')
        print(f'Humidity: {weather_data["humidity"]}')
        print(f'Wind Speed: {weather_data["wind_speed"]}')


