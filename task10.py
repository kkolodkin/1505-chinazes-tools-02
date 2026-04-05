import requests

def task_10():
    print("\n--- Случайная цитата ---")
    response = requests.get("https://api.quotable.io/random")
    data = response.json()
    print(f"\"{data['content']}\"\n— {data['author']}")

task_10()