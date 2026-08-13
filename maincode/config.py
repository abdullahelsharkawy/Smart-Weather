# This module stores the application's configuration 
from dotenv import load_dotenv
import os

load_dotenv()

App_name = os.getenv("App_name","Abdullah Project")      # fallback value

Openweather_API = os.getenv("API_key")










if __name__ == "__main__":
    print(f"Application Name : {App_name}")
    if Openweather_API:
        print("Found Syccessfully")
    else:
        print("API Key was not Found")

        





