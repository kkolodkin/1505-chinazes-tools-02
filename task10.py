import requests

def run():
    print("\n--- Случайная цитата ---")
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    print(f"\"{data['content']}\"\n— {data['author']}")

run()
