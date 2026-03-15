from random import sample
import string
d=string.digits
game='y'
while game=='y':
    m=sample(d,4)
    s=''
    for i in range(4):
        s=s+str(m[i])
    cnt=1
    n=input('Попробуй угадать четырехзначное число:')
    nflag=1
    for i in n:
        if i not in d:
            nflag=0
            break
    if len(n)==4 and nflag==1:
        while n!=s:
            cnt+=1
            bull=0
            cow=0
            for i in range(4):
                if n[i]==s[i]:
                    bull+=1
                elif s.count(n[i])==1:
                    cow+=1
            print(n, ':', 'быки -', bull, '   коровы -', cow)
            n=input('Попробуй угадать четырехзначное число:')
        print('Поздравляю! Ты угадал число', *s, 'за', cnt, 'попыток!')
        game=input('Сыграть ещё раз? y/n:')
        
