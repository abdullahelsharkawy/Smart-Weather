"""
in this file display poject
"""
from Advisor import temperature_recommend
from Advisor import weather_recommend
import weather
def show_pro():

    print("\n*****WELCOME TO SMART WEATHER*****\n")
    city_user = input("Weather Your City : ")
    print("\n")
    
    data = weather.main(city = city_user)

    print("-"*30)
    print(f"Temperature : {data["temperature"]} ℃ ")
    print(f"Weather : {data["condition_group"]} ")
    print(f"Humidity : {data["Humidity"]} %")
    print(f"Wind Speed : {data["windspeed"]} m/s")
    print("-"*30)


    print(f"""
Recommedations:
    {temperature_recommend(city= city_user)}

    ----------------------------------

Note:
    {weather_recommend(city= city_user)}

    """)


if __name__ =="__main__":
    show_pro()

