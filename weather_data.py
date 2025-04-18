import requests

def get_simple_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        print("\n🌦️", response.text if response.status_code == 200 else "Error fetching data.")
    except:
        print("\n❌ Network or connection issue.")

def get_full_ascii_weather(city):
    url = f"https://wttr.in/{city}"
    try:
        response = requests.get(url)
        print(response.text if response.status_code == 200 else "Error fetching data.")
    except:
        print("\n❌ Couldn't reach wttr.in")


def get_json_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            print(f"\n📍 City: {city}")
            print(f"🌡️ Temperature: {current['temp_C']}°C")
            print(f"💧 Humidity: {current['humidity']}%")
            print(f"🌬️ Wind: {current['windspeedKmph']} km/h")
            print(f"🌥️ Condition: {current['weatherDesc'][0]['value']}")
        else:
            print("\n❌ Error fetching weather data.")
    except:
        print("\n❌ Failed to connect or parse data.")



print("=== 🌤️ Quick Weather (No API Key) ===")
city = input("Enter city name: ")
get_simple_weather(city)
get_full_ascii_weather(city)
get_json_weather(city)
