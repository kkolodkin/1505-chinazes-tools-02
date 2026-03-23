import requests
def run():
    url = "https://api.open-meteo.com/v1/forecast?latitude=55.7558&longitude=37.6176&current_weather=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        current = data.get("current_weather", {})
        temp = current.get("temperature")
        wind_speed = current.get("windspeed")
        print("--- Текущая погода в Москве ---")
        print(f"Температура: {temp}°C")
        print(f"Скорость ветра: {wind_speed} км/ч")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при подключении к API: {e}")
if __name__ == "__main__":
    run()
