import requests


def fetch_weather(city):
    """
    City to weather using wttr.in (free, no API key needed)
    :param city: City
    :return: weather string
    """
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)
        data = response.json()

        current = data["current_condition"][0]
        weather_description = current["weatherDesc"][0]["value"]
        current_temperature = current["temp_C"]
        current_humidity = current["humidity"]
        current_pressure = current["pressure"]
        wind_speed = current["windspeedKmph"]

        final_response = (
            f"The weather in {city} is currently {weather_description} "
            f"with a temperature of {current_temperature} degree celsius, "
            f"atmospheric pressure of {current_pressure} hectoPascals, "
            f"humidity of {current_humidity} percent "
            f"and wind speed reaching {wind_speed} kilometers per hour"
        )
        return final_response

    except Exception as e:
        print(e)
        return "Sorry Sir, I couldn't fetch the weather. Please try again"