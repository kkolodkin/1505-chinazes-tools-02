import requests

def task_11():
    print("\n--- Случайный совет ---")
    response = requests.get("https://api.adviceslip.com/advice")
    data = response.json()
    print(f"Совет: {data['slip']['advice']}")

task_11()
