from random import sample
import string
def run():
    digits=list(string.digits)
    game='y'
    while game=='y':
        m=sample(digits,4)
        s=''
        for i in range(4):
            s=s+str(m[i])
        cnt=1
        n=input('Попытайтесь угадать четырехзначное число:')
        nflag=1
        if len(n)!=4:
            nflag=0
        for i in n:
            if i not in digits:
                nflag=0
                break
        while nflag==0:
            print('Это не четырёхзначное число!')
            n=input('Попытайтесь угадать ЧЕТЫРЁХЗНАЧНОЕ ЧИСЛО:')
            nflag=1
            if len(n)!=4:
                nflag=0
            for i in n:
                if i not in digits:
                    nflag=0
                    break
        while n != s:
            cnt+=1
            bull=0
            cow=0
            for i in range(4):
                if n[i]==s[i]:
                    bull+=1
                elif s.count(n[i])==1:
                    cow+=1
            print(n, ': быки -', bull, '    коровы -', cow)
            n=input('Попытайтесь угадать четырехзначное число:')
            nflag=1
            if len(n)!=4:
                nflag=0
            for i in n:
                if i not in digits:
                    nflag=0
                    break
            while nflag==0:
                print('Это не четырёхзначное число!')
                n=input('Попытайтесь угадать ЧЕТЫРЁХЗНАЧНОЕ ЧИСЛО:')
                nflag=1
                if len(n)!=4:
                    nflag=0
                for i in n:
                    if i not in digits:
                        nflag=0
                        break
        print('Поздравляю! Ты угадал число', s, 'за', cnt, 'попыток!')
        game=input('Сыграть ещё раз? y/n:')
        while game!='y' and game != 'n':
            print('Некорректый ввод!')
            game=input('Сыграть ещё раз? y/n:')
if __name__ == "__main__":
    run()
