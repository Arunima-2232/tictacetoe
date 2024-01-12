# to make tic tac toe on python
# required
# the box, put X and O on the box in the correct position, before putting check if that position is empty or not
# 2 players each player gets one chance, player can only put X or O, can only put one in one chance, can only put inside box

# making the box
def box():

    print()
    print("\t ____________________")
    print("\t|      |      |      |")  
    print("\t|      |      |      |")  
    print('\t|______|______|______|')
    print("\t|      |      |      |")  
    print("\t|      |      |      |")  
    print('\t|______|______|______|')
    print("\t|      |      |      |")  
    print("\t|      |      |      |")  
    print('\t|______|______|______|')
    print()

# scoreboard
def score_board():
    print("SCOREBOARD \n")
    score={'P1':0,'P2':0}
    for i in score:
        print(i,":",score[i])

# intro to game
def main():
    # create another function for instructions
    print()

    #take names
    player_1=input("Enter username for Player 1: ")
    player_2=input("Enter username for Player 2: ")
    di={'X':'','O':''}
    print()

    # allot X or O according to input
    print(player_1, "choose between 'X' and 'O': ",end=" ")
    symbol=input()
    # CHANGE: Player_1 should be displayed first
    di[symbol]=player_1
    for i in di.keys():
        if di[i]=='':
            di[i]=player_2
    print("\n")
    for i in di.keys():
        print(di[i], "has chosen", i)

main()
box()
score_board()
