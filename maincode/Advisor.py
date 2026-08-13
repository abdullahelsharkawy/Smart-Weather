"""
To Make recommendations based on weather conditions
"""

import weather

def temperature_recommend(city):
    data = weather.main(city)

    if data["temperature"] < 10:
        return ("The Weather is Vary Cold \n \
                clothes: Heavy Jacket, sweater, and warm pants"
        )
    elif data["temperature"] < 18:
        return ("The Weather Is Cold \n \
                Clothes:  Jacket, and long pants"
        )
    elif data["temperature"] < 25:
        return (
            "The Weather Is Moderate \n \
            Clothes:  light Jacket, and lond-sleeve shirt and pants "
        )
    elif data["temperature"] < 32:
        return ("The Weather Is Vary Moderate \n \
                Clothes: T-shirt and light pants"
        )
    else:
        return "The weather Is Hot \n \
             Clothes: Vary light clothes"


def weather_recommend(city):
    data = weather.main(city)
    if data["condition_group"].lower() == "thunderstorm":
        return "Severe thunderstorm hazard!"

    elif data["condition_group"].lower() in ["rain", "drizzle"]:
        return "It is raining outside, carry a sturdy umbrella."

    elif data["condition_group"].lower() == "snow":
        return "Heavy snow or freezing weather."

    elif data["condition_group"].lower() in [
        "mist",
        "smoke",
        "haze",
        "dust",
        "fog",
        "sand",
        "ash",
        "squall",
        "tornado",
    ]:
        if data["condition_group"] == "tornado":
            return f"TORNADO WARNING!, Keep Yourself or Stay  Out!"
        return f"Reduced visibility due to {data["condition_group"]}"

    elif data["condition_group"].lower() == "clear":
        if 20 <= data["temperature"] <= 28:
            return "Beautiful clear sky!"
        elif data["temperature"] > 35:
            return "Clear Sky but extremely hot."
        else:
            return "Clear sky"

    elif data["condition_group"].lower() == "clouds":
        if data["windspeed"] > 25:
            return "Cloudy and windy"
        return "Pleasant overcast sky"

    else:
        return "Weather conditions are stable for normal daily routines"
