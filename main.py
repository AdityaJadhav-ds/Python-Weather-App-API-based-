import requests

API_KEY = "YOUR_API_KEY" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"{data['main']['temp']}°C, {data['weather'][0]['description']}")
    else:
        print("Error:", data.get("message", "Something went wrong."))

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
