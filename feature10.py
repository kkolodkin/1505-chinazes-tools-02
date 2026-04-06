import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def run():
    print("\n--- Случайная цитата ---")
    response = requests.get("https://api.quotable.io/random", verify=False)
    data = response.json()
    print(f"\"{data['content']}\"\n— {data['author']}")

if __name__ == "__main__":
    run()
