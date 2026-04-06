import feature1,feature2,feature3,feature4,feature5
import feature6,feature7,feature8,feature9,feature10
import feature11,feature12,feature13


def print_menu():
    print(
'''
============================
Menu options

1. Number guess game
2. Bulls and cows game
3. Tic-tac-toe game
4. Rock, Paper, Scissors game
5. Quiz game
6. Password Generator
7. Random Number Generator
8. Encryptor/Decryptor
9. Weather in Moscow
10.Random Quote
11.Random Advice
12.Random Joke About Programmers
13.Random Fact
14.Russian-English translator
15. Exit

============================
''')

print("Hello! Welcome to Chinazes Tools!")

while 1:
    print_menu()
    user_choice = input("Select a menu option number: ")
    print()
    
    if user_choice == '1':
        feature1.run()
    elif user_choice == '2':
        feature2.run()
    elif user_choice == '3':
        feature3.run()
    elif user_choice == '4':
        feature4.run()
    elif user_choice == '5':
        feature5.run()
    elif user_choice == '6':
        feature6.run()
    elif user_choice == '7':
        feature7.run()
    elif user_choice == '8':
        feature8.run()
    elif user_choice == '9':
        feature9.run()
    elif user_choice == '10':
        feature10.run()
    elif user_choice == '11':
        feature11.run()
    elif user_choice == '12':
        feature12.run()
    elif user_choice == '13':
        feature13.run()
    elif user_choice == '15':
        print("Bye!")
        break
    elif user_choice == '14':
        print("This option is comming soon...")
    else:
        print("Invalid choice. Try again.")
