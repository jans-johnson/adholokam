# ------- Global variables

var='X'
#gameboard
board=["-","-","-",
       "-","-","-",
       "-","-","-",]

#game is still going
game_still_going=True

#function to display board
def display():
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])

#to enter the position

def entry():
    global var
    if(var=='X'):
        z=int(input("Player 1:Enter position (1-9) for "+var+":"))
    elif(var=='O'):
        z=int(input("Player 2:Enter position (1-9) for "+var+":"))
    board[z-1]=var

#to switch the variables

def switch():
    global var
    if(var=='X'):
        var='O'
    else:
        var='X'

#checking by row

def check_row():
    global game_still_going
    
    if(board[0]==board[1] and board[1]==board[2]):
        if(board[0]!='-'):
            game_still_going=False
            return board[0]
    elif(board[3]==board[4] and board[4]==board[5]):
        if(board[3]!='-'):
            game_still_going=False
            return board[3]
    elif(board[6]==board[7] and board[7]==board[8]):
        if(board[6]!='-'):
            game_still_going=False
            return board[6]            
#checking by column

def check_column():
    global game_still_going
    if(board[0]==board[3] and board[3]==board[6]):
        if(board[0]!='-'):
            game_still_going=False
            return board[0]
    elif(board[1]==board[4] and board[4]==board[7]):
        if(board[1]!='-'):
            game_still_going=False
            return board[1]
    elif(board[2]==board[5] and board[5]==board[8]):
        if(board[2]!='-'):
            game_still_going=False
            return board[2]

#checking by diagonal

def check_diagonal():
    global game_still_going
    if((board[0]=='-')or(board[2]=='-')):
        return
    elif(board[0]==board[4]):
        if(board[4]==board[8]):
            if(board[0]=='X'):
                print("Player 1 Won by Diagonal")
            elif(board[0]=='O'):
                print("Player 2 won by diagonal")
    elif(board[2]==board[4]):
        if(board[4]==board[6]):
            if(board[2]=='X'):
                print("Player 1 won by diagonal")
            elif(board[2]=='X'):
                print("Player 2 won by diagonal")                    
#function to check for the win

def check_win():
    x=0
    y=0
    x=check_row()
    y=check_column()
    check_diagonal()
    if((x!=0) or (y!=0)):
        if(x=='X'):
            print("Player 1 win by row")
        elif(x=='O'):
            print("Player 2 win by row")    
        elif(y=='X'):
            print("Player 1 win by column")
        elif(y=='O'):
            print("Player 2 win by column")        

#to check if match is tie

def check_tie():
    for i in range(9):
        if(board[i]=='-'):
            return False
    print("Game is a tie!!")


#function calling

while(game_still_going):
    display()
    entry()
    check_win()
    switch()
display()

