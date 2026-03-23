import urllib.request
import urllib.error
import json
import random

def get_question():
    url = "https://the-trivia-api.com/v2/questions"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        if data:
            return data[0]
        else:
            print("Не удалось получить вопрос.")
            return None
    except urllib.error.URLError as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

def display_question(question_data):
    question_text = question_data['question']['text']
    correct_answer = question_data['correctAnswer']
    incorrect_answers = question_data['incorrectAnswers']
    
    options = incorrect_answers + [correct_answer]
    random.shuffle(options)
    
    print(f"\nВопрос: {question_text}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    return options, correct_answer

def run():
    score = 0
    print("Добро пожаловать в викторину!")
    
    while True:
        question_data = get_question()
        if not question_data:
            break
        
        options, correct_answer = display_question(question_data)
        
        try:
            choice = int(input("Ваш ответ (введите номер варианта): "))
            if 1 <= choice <= len(options):
                if options[choice - 1] == correct_answer:
                    print("Правильно! +1 очко")
                    score += 1
                else:
                    print(f"Неправильно. Правильный ответ: {correct_answer}")
            else:
                print("Неверный номер варианта. Попробуйте ещё раз.")
                continue
        except ValueError:
            print("Пожалуйста, введите число.")
            continue
        
        print(f"Ваш счёт: {score}")
        
        again = input("Хотите продолжить? (да/нет): ").strip().lower()
        if again not in ['да', 'lf', 'yes', 'y']:
            print(f"Игра окончена. Ваш итоговый счёт: {score}")
            break

if __name__ == "__main__":
    run()
