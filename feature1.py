from random import randint
import string
def run():
    game='y'
    digits=list(string.digits)
    while game=='y':
        a=input('Введите нижний порог диапазона загадывания:')
        b=input('Введите верхний порог диапазона загадывания:')
        aflag=1
        bflag=1
        for i in a:
            if i not in digits and i!='-':
                aflag=0
                break
        for i in b:
            if i not in digits and i!='-':
                bflag=0
                break
        if aflag+bflag==2 and a!='-' and b!='-':
            a=int(a)
            b=int(b)
            if a in range(-(10**10),10**10) and b in range(-(10**10),10**10) and a<b:
                s=randint(a,b)
                cnt=1
                n=input('Попытайтесь угадать число:')
                nflag=1
                for i in n:
                    if i not in digits and i !='-':
                        nflag=0
                        break
                while nflag==0:
                    print('Это не число!')
                    n=input('Попытайтесь угадать ЧИСЛО:')
                    nflag=1
                    for i in n:
                        if i not in digits:
                            nflag=0
                            break
                n=int(n)
                while n != s:
                    cnt+=1
                    if s>n:
                        print('Моё число больше')
                    else:
                        print('Моё число меньше')
                    n=input('Попытайтесь угадать число:')
                    nflag=1
                    for i in n:
                        if i not in digits and i !='-':
                            nflag=0
                            break
                    while nflag==0:
                        print('Это не число!')
                        n=input('Попытайтесь угадать ЧИСЛО:')
                        nflag=1
                        for i in n:
                            if i not in digits:
                                nflag=0
                                break
                    n=int(n)
                print('Поздравляю! Ты угадал число за', cnt, 'попыток')
                game=input('Сыграть ещё раз? y/n:')
                while game!='y' and game != 'n':
                    print('Некорректый ввод!')
                    game=input('Сыграть ещё раз? y/n:')
            else:
                if a not in range(-(10**10),10**10) or b not in range(-(10**10),10**10):
                    print('Слишком большой диапазон!')
                if a>b:
                    print('Нижний порог больше чем верхний!')
        else:
            print('Некорректный ввод диапазона!')
            
if __name__ == "__main__":
    run()
