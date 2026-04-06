"""Task 13: Random Fact"""
import requests


def run():
    print("=== Случайный Факт ===")

    try:
        response = requests.get(
            'https://uselessfacts.jsph.pl/random.json?language=en',
            timeout=15  
        )
        response.raise_for_status()
        data = response.json()

        if 'text' in data:
            print(f"\n📚 {data['text']}")
        else:
            print("Не удалось получить факт")

    except requests.exceptions.Timeout:
        print("⏱️ Ошибка: Сервер не ответил (таймаут). "
              "Попробуйте еще раз позже.")
    except requests.exceptions.ConnectionError:
        print("🔌 Ошибка подключения. Проверьте интернет-соединение.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ Ошибка HTTP: {e}")
    except requests.RequestException as e:
        print(f"⚠️ Ошибка при запросе: {e}")



if __name__ == "__main__":
    run()
