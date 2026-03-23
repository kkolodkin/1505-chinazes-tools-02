import random
def run():
    """Main rock paper scissors game."""
    choices = ['камень', 'ножницы', 'бумага']
    choice_map = {
        'к': 'камень',
        'н': 'ножницы',
        'б': 'бумага',
        '1': 'камень',
        '2': 'ножницы',
        '3': 'бумага'
    }

    def check_winner(player_choice, computer_choice):
        """Check the winner."""
        if player_choice == computer_choice:
            return "Ничья!"

        if (player_choice == 'камень' and computer_choice == 'ножницы' or
            player_choice == 'ножницы' and computer_choice == 'бумага' or
            player_choice == 'бумага' and computer_choice == 'камень'):
            return "Вы выиграли! 🎉"

        return "Компьютер выиграл! 💻"

    while True:
        print("\n=== Камень, ножницы, бумага ===")
        print("Введите (к)амень, (н)ожницы или (б)умага")
        print("Или 1-камень, 2-ножницы, 3-бумага")

        player_input = input("Ваш ход: ").lower().strip()

        if player_input not in choice_map:
            print("Некорректный ввод. Попробуйте еще раз.")
            continue

        player_choice = choice_map[player_input]
        computer_choice = random.choice(choices)

        print(f"\nВы выбрали: {player_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        print(check_winner(player_choice, computer_choice))

        play_again = input("\nИграть еще? (да/нет): ").lower()
        if play_again not in ['да', 'yes', 'y']:
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    run()
