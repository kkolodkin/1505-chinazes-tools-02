import random
player_symbols = ' OX'
rows = 'ABC'
columns = '123'
cords=[rows[i]+columns[j] for i in range(3) for j in range(3)]

def board(gm):
    cntr=0
    print('  1   2   3')
    for row in gm:
        print(rows[cntr],end=' ')
        cntc=0
        for cell in row:
            if cntc<2:
                print(player_symbols[cell], end=' | ')
            else:
                print(player_symbols[cell])
            cntc+=1
        if cntr<2:
            print('  - + - + -')
        cntr+=1
        
def is_tie(gm):
    for row in gm:
        for cell in row:
            if cell == 0:
                return False
    return True

def is_win(gm):
    if gm[1][1]!=0:                     # 3 in diagonal
        if gm[0][0]==gm[1][1]==gm[2][2] or gm[0][2]==gm[1][1]==gm[2][0]:
            return gm[1][1]
    for i in range(3):
        if gm[0][i] != 0:               # 3 in vertical
            if gm[0][i]==gm[1][i]==gm[2][i]:
                return gm[0][i]
        if gm[i][0] != 0:               # 3 in horizontal
            if gm[i][0]==gm[i][1]==gm[i][2]:
                return gm[i][0]
    return False

def player_input(gm, player):
    print('Ваш ход! Вы играете за',player_symbols[player])
    move=input('Выберите клетку:').capitalize()
    while move not in cords:
        print('Такой клетки не существует! Формат: A1')
        move=input('Выберите существующую клетку:').capitalize()
    while gm[rows.index(move[0])][columns.index(move[1])] != 0:
        print('Эта клетка уже занята!')
        move=input('Выберите пустую клетку:').capitalize()
        while move not in cords:
            print('Такой клетки не существует! Формат: A1')
            move=input('Выберите существующую пустую клетку:').capitalize()
    gm[rows.index(move[0])][columns.index(move[1])] = player
    return gm

def bot_input(gm, bot, player, stepcnt):
    if gm[1][1]==0:
        gm[1][1]=bot
        return gm
    ### late logic
    for check in [bot,player]:
        ### diag check
        diag=[gm[0][0],gm[1][1],gm[2][2]]
        if set(diag)=={0,check} and diag.count(check)==2:
            gm[diag.index(0)][diag.index(0)]=bot
            return gm
        ### inverse diag check
        invdiag=[gm[0][2],gm[1][1],gm[2][0]]
        if set(invdiag)=={0,check} and invdiag.count(check)==2:
            gm[invdiag.index(0)][2-invdiag.index(0)]=bot
            return gm
        ### columns check
        for i in range(3):
            column=[]
            for row in gm:
                column.append(row[i])
            if set(column)=={0,check} and column.count(check)==2:
                gm[column.index(0)][i]=bot
                return gm
        ### rows check
        for i in range(3):
            row=gm[i]
            if set(row)=={0,check} and row.count(check)==2:
                gm[i][row.index(0)]=bot
                return gm
    ### eariy logic
    if stepcnt == 2:
        gm[random.sample([0,2],1)[0]][random.sample([0,2],1)[0]]=bot
        return gm
    if stepcnt == 3:
        if player in [gm[0][0],gm[0][1],gm[1][0]]:
            gm[2][2]=bot
            return gm
        elif player in [gm[2][2],gm[2][1],gm[1][2]]:
            gm[0][0]=bot
            return gm
        elif gm[0][2] == player:
            gm[2][0] = bot
            return gm
        elif gm[2][0] == player:
            gm[0][2] = bot
            return gm
    # random move
    zeroes=[]
    for y in range(3):
        for x in range(3):
            if gm[y][x]==0:
                zeroes.append([y,x])
    move=random.sample(zeroes,1)
    gm[move[0][0]][move[0][1]]=bot
    return gm

def run():
    game='y'
    while game=='y':
        gm=[[0,0,0],[0,0,0],[0,0,0]]
        stepcnt=0
        first=input('Чей ход первый? player/bot/random:')
        variants=['player','p','1','bot','b','2','random','r','3']
        while first not in variants:
            print('Некорректный ввод!')
            first=input('Чей ход первый? player/bot/random:')
        if first in [variants[i] for i in range(6,9)]:
            first = random.sample(['p','b'],1)
        if first in [variants[i] for i in range(3,6)]:
            bot=-1
            player=1
            stepcnt+=1
            gm[1][1]=bot
        else:
            bot=1
            player=-1
        board(gm)
        while is_tie(gm)==False and is_win(gm)==False:
            stepcnt+=1
            gm=player_input(gm, player)
            board(gm)
            if is_tie(gm)== True or is_win(gm)!=False:
                break
            print('Ход бота:')
            stepcnt+=1
            gm=bot_input(gm, bot, player, stepcnt)
            board(gm)
        if is_tie(gm)==True:
            print('Ничья!')
        else:
            if is_win(gm)==player:
                print('Ура! Вы победили!')
            else:
                print('Вы проиграли...')
        game=input('Хотите сыграть ещё раз? y/n:')
        while game!='y' and game != 'n':
            print('Некорректный ввод!')
            game=input('Хотите сыграть ещё раз? y/n:')
run()
