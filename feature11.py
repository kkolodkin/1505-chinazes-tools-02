import requests

def run():
    print("\n--- Случайный совет ---")
    response = requests.get("https://api.adviceslip.com/advice")
    data = response.json()
    print(f"Совет: {data['slip']['advice']}")

if __name__ == "__main__":
    run()
