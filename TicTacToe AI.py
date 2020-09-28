turn=-1
board=[[" " for i in range(3)] for j in range(3)]
players=["X","O"]
stillplaying=True

def playerturn():
    global board
    board[int(input("Row:"))][int(input("Col:"))]=players[turn%2]
    print()
    printboard(board)

def randomturn():
    global board,turn
    r=random.randint(0,2)
    c=random.randint(0,2)
    while board[r][c]!=" ":       
        r=random.randint(0,2)
        c=random.randint(0,2)
    board[r][c]=players[turn%2]
    printboard(board)

def AIturn():
    global board,start
    player=players[turn%2]
    for k in range(2):
        for i in range(3):
            for j in range(3):
                tempboard=board.copy()
                if tempboard[i][j]==" ":
                    tempboard[i][j]=player
                    if wincond(tempboard,player):
                        board[i][j]=players[turn%2]                       
                        printboard(board)
                        return
                    tempboard[i][j]=" "
        player=players[(turn+1)%2]

    if turn%2==0:
        if turn==8:
            for i in range(3):
                for j in range(3):
                    if board[i][j]==" ":
                        board[i][j]=players[turn%2]
                        break
        elif turn==0:
            board[0][0]=players[turn%2]
        elif turn==2:
            if board[1][1]==players[(turn+1)%2]:
                board[1][2]=players[turn%2]
            elif any(board[item[0]][item[1]]==players[(turn+1)%2] for item in [[0,1],[0,2],[1,2]]):
                board[2][0]=players[turn%2]
            else:
                board[0][2]=players[turn%2]
        elif turn==4:
            if board[1][1]==players[(turn+1)%2] and(board[1][0]==players[(turn+1)%2] or board[2][2]==players[(turn+1)%2]):
                board[0][2]=players[turn%2]
            elif board[2][2]==players[(turn+1)%2]:
                board[2][0]=players[turn%2]
            else:
                board[2][2]=players[turn%2]
        
    else:
        if turn==1:
            if board[1][1]==" ":
                board[1][1]=players[turn%2]               
            elif board[0][0]==" ":
                board[0][0]=players[turn%2]
        elif turn==3:
            if board[1][1]==players[(turn+1)%2]:
                board[0][2]=players[turn%2]
            elif (board[0][2]==players[(turn+1)%2] and board[2][0]==players[(turn+1)%2]) or (board[0][0]==players[(turn+1)%2] and board[2][2]==players[(turn+1)%2]):
                board[0][1]=players[turn%2]
            elif (board[0][1]==players[(turn+1)%2] and board[2][1]==players[(turn+1)%2]) or (board[1][0]==players[(turn+1)%2] and board[1][2]==players[(turn+1)%2]):
                board[0][0]=players[turn%2]
            else:
                for i in range(4):
                    if board[[0,1,2,1][i]][[1,0,1,2][i]]==players[(turn+1)%2]:
                        if board[[1,0,1,2][i]][[2,1,0,1][i]]==players[(turn+1)%2]:
                            board[[2,0,0,2][i]][[2,2,0,0][i]]=players[turn%2]
                        elif board[[2,0,0,2][i]][[2,2,0,0][i]]==players[(turn+1)%2]:
                            board[[1,2,1,0][i]][[0,1,2,1][i]]=players[turn%2]
                        else:
                            board[[1,0,1,2][i]][[2,1,0,1][i]]=players[turn%2]
        else:
            for i in range(4):
                if board[[0,1,2,1][i]][[1,0,1,2][i]]==" ":
                    board[[0,1,2,1][i]][[1,0,1,2][i]]=players[turn%2]
                    break
    printboard(board)

def printboard(board):
    global turn
    print("\n-+-+-\n".join([("|".join(str(board[i][j]) for j in range(3))) for i in range(3)])+"\n")
    turn+=1

def wincond(board,player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3)) or all(board[j][i]==player for j in range(3)) or all(board[j][j]==player for j in range(3)) or all(board[3-j-1][j]==player for j in range(3)):
            return True
    return False

def run(func):
    global stillplaying
    if stillplaying:
        if func=="A":
            AIturn()
        elif func=="P":
            playerturn()
        else:
            randomturn()
        if wincond(board,players[(turn+1)%2]):
            stillplaying=False
            print(players[(turn+1)%2]+" Wins!")

turns=input("What players would you like to play. (A,P,R)")

printboard(board)

while stillplaying:
    run(turns[turn%2])
    if turn==9:
        print("Cats Game")
        stillplaying=False
