import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\n🌦️", response.text)
        else:
            print("\n❌ Could not fetch weather.")
    except:
        print("\n❌ An error occurred while fetching weather data.")

print("=== 🌤️ Simple Weather App (No API Key Needed :) ) ===")
city = input("Enter a city name: ")
get_weather(city)