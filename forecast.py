import requests

api_key = "b4167a1d839961bc58b451c102d042b6"


def weather_forecast(city):
    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
    result = dict(result.json())
    temperature = float(result['main']['temp']) - 273.15
    weather = result['weather'][0]['description']
    return list([temperature, weather])
