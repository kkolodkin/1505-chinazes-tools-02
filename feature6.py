import random
import string
 
 
def run():
   """Main password generator."""
   print("\n=== Генератор Паролей ===")
 
   
   while True:
       try:
           length = int(input("Введите длину пароля (1-100): "))
           if 1 <= length <= 100:
               break
           print("Длина должна быть от 1 до 100")
       except ValueError:
           print("Введите корректное число")
 
   
   use_digits = input("Использовать цифры? (да/нет): ").lower() in \
                ['да', 'yes', 'y','1']
   use_special = input("Использовать спец. символы? (да/нет): ").lower() in \
                 ['да', 'yes', 'y','1']
   use_uppercase = input("Использовать заглавные буквы? (да/нет): ").lower() \
                   in ['да', 'yes', 'y','1']
 

   characters = string.ascii_lowercase
   if use_uppercase:
       characters += string.ascii_uppercase
   if use_digits:
       characters += string.digits
   if use_special:
       characters += "!@#$%^&*()_+{}:\"<>?,./;'[]\\|/\"`~"
 
   if not characters:
       characters = string.ascii_lowercase
 
   
   password = ''.join(random.choice(characters) for _ in range(length))
 
   print(f"\nВаш пароль: {password}")
   print(f"Длина: {length}")
 
 
if __name__ == "__main__":
   while True:
       run()
       again = input("\nГенерировать еще? (да/нет): ").lower()
       if again not in ['да', 'yes', 'y','1']:
           break
