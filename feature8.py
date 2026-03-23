def run():
    s = input("Введите сообщение: ")
    flag = True
    while flag:
        try:
            n = int(input("Введите ключ(для шифровки числа больше 0, для дешифровки числа меньше нуля: "))
            flag = False
        except:
            print('Ошибка ввода данных!')
            
    res = ""
    for i in s:
        if 'a' <= i <= 'z':
            res += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif 'A' <= i <= 'Z':
            res += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif 'а' <= i <= 'я':
            res += chr((ord(i) - ord('а') + n) % 32 + ord('а'))
        elif 'А' <= i <= 'Я':
            res += chr((ord(i) - ord('А') + n) % 32 + ord('А'))
        else:
            res += i
    print("Зашифрованное сообщение:", res)
if __name__ == "__main__":
    run()
