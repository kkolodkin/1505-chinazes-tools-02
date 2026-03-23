import random
def run():
    flag = True
    while flag:
        try:
            a = int(input('Введите кол-во чисел:'))
            b, c = map(int, input('Введите диапозон чисел через пробел:').split())
            if a > 0 and b < c and a < 1001 and -(10**10) < b < 10 ** 10 and -(10**10)<c< 10**10:
                for _ in range(a):
                    print(random.randint(b, c))
                flag = False
            else:
                print('Ошибка ввода данных!!!')
        except ValueError:
            print('Ошибка ввода данных!!!')
run()
