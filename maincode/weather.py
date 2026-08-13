# # get the weather data from API and return to main.py
# # API is Openweathermap API

"""\nHi,We are Here untill Fetch Weather Data from openweather\n"""

import sys
import requests
import rich
import config


def main(city):

    try:
       return fetch_data(city)

    except requests.HTTPError:
        print("There is error in your URL, Check it well")
        sys.exit()

    except requests.ConnectionError:
        print( "There is NOT Internet Connection , Check it well")
        sys.exit()





def fetch_data(dd):
    URL = "https://api.openweathermap.org/data/2.5/weather"

 
    parameters = {
        "q": dd,
        "appid": config.Openweather_API,
        "units": "metric",
    }

    response = requests.get(URL, params=parameters, timeout=5)
    response.raise_for_status()

    

    data = response.json()


    temperature_max = data["main"]["temp"]
    temperature_min = data["main"]["temp_min"]
    Humidity = data["main"]["humidity"]
    windspeed = data["wind"]["speed"]
    weather_condition = data["weather"][0]["main"]
    temperature = data["main"]["feels_like"]

# Directly, can return dectionary After analysis Process . (1 step )

    return {
        "max_temperature" : temperature_max ,
        "min_temperature" : temperature_min ,
        "Humidity" : Humidity ,
        "windspeed" : windspeed ,
        "condition_group" : weather_condition ,
        "temperature" : temperature ,
    }
    

    


if __name__ == "__main__":
    print("Welcome To You in Weather code ")
    city_test = input("Enter The city :")
    rich.print(main(city_test))
    # print(main())

