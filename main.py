"""
Задание 14: Русско-английский переводчик.

Разработчик:
Тестировщик:
Ответственный за CR:
"""

import urllib.request
import urllib.parse
import json
import ssl


def run():
    """Запрашивает текст на английском и переводит его на русский."""
    print("Переводчик: Английский → Русский")

    text = input("Введите текст на английском (до 200 символов): ").strip()

    if not text or len(text) > 200:
        print("Ошибка: текст пустой или превышает 200 символов.")
        return

    params = urllib.parse.urlencode({"q": text, "langpair": "en|ru"})
    url = f"https://api.mymemory.translated.net/get?{params}"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    with urllib.request.urlopen(url, timeout=10, context=ctx) as response:
        data = json.loads(response.read().decode("utf-8"))

    print("Перевод:", data["responseData"]["translatedText"])


if __name__ == "__main__":
    run()
