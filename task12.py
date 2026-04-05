import requests

def task_12():
    print("\n--- Шутка ---")
    response = requests.get("https://v2.jokeapi.dev/joke/Programming")
    data = response.json()
    
    if data['type'] == 'single':
        print(data['joke'])
    else:  
        print(f"{data['setup']}\n{data['delivery']}")

task_12()
