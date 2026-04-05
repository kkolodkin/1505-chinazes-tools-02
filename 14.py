def task_14_translate():
    print("---Переводчик (En -> Ru) ---")
    text = input("Введите текст на английском (до 200 символов): ")
    if len(text) > 200:
        print("Текст слишком длинный.")
        return
        
    url = f"https://ftapi.pythonanywhere.com/translate?sl=en&dl=ru&text={text}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Перевод: {response.text}")
        else:
            print(f"Ошибка сервера: {response.status_code}")
    except Exception as e:
        print(f"Ошибка соединения: {e}")

print(task_14_translate)
