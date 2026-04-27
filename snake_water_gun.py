from random import choice
from getpass import getpass
from time import sleep
from os import system,name
from datetime import datetime
# from sup import clear_output

    


def game(uc,rc):
    if uc==rc:
        return 0
    elif uc=="s" and rc=="w":
        return 1
    elif uc=="s" and rc=="g":
        return -1 
    elif uc=="w" and rc=="s":
        return -1
    elif uc=="w" and rc=="g":
        return 1
    elif uc=="g" and rc=="s":
        return 1
    elif uc=="g" and rc=="w":
        return -1

def real(u):
    if u == "s":
        real = "SNAKE"
    elif u == "w":
        real = "WATER"
    elif u == "g":
        real = "GUN"
    return real

def swg(ui):
    if ui=="s" or ui=="w" or ui=="g":
        pass
    elif ui!="s" or ui!="w" or ui!="g":
        return 1

def clear_output(): # This fuction will clear previous outputs!
	if name=="nt": # For windows
		_=system("cls")
	else: # For others OS
		_=system("clear")
        

class Player:
    def __init__(self,name) -> None:
        self.name = name

    # def choice(self,choice):
    #     self.choice = choice



print("         Snake~Water~Gun game\n")
print("        ",datetime.now())
print("\nHow do you wanna play this game?\n1 : Player V/S Computer\n2 : Player 1 V/S Player 2")
fi=int(input("1 or 2?\n"))
try:
    rounds=int(input("How many rounds you wanna play : ")) # i was here!
except Exception as e:
    print("Restart the programme :",e)
    
clear_output()

win=0
win_1=0
win_2=0
lose=0
draw=0
fullDate=datetime.now()


if fi==2:
    player_1=input("Enter Player one's name : ")
    player1 = Player(player_1)
    player_2=input("Enter Player two's name : ")
    player2 = Player(player_2)
    print("Note: Player one's input isn't shown in the game.")
    print("Loading.")
    sleep(1)
    print("Loading..")
    sleep(1)
    print("Loading...")
    clear_output()
    z=1
    while z<=rounds:
        print("ROUND :",z)
        print(z*"*")
        plr_1=getpass(f"{player_1}'s turn :\nSnake[S],Water[W] or Gun[G] : ").lower()
        plr_2=input(f"{player_2}'s turn :\nSnake[S],Water[W] or Gun[G] : ").lower()

        clear_output() #clearing output over here!
        if swg(plr_1)==1:
            if swg(plr_2)==1:
                print("Invalid Input for both of the players!\nTry Again Players!")
                continue
            print("Invalid Input from player one:",player_1)
            print("Try again!")
            continue
        if swg(plr_2)==1:
            print("Invalid Input from player two:",player_2)
            print("Try again!")
            continue
        z+=1
        rel_1=real(plr_1)
        rel_2=real(plr_2)
        g=game(plr_1,plr_2)
        print("__________________________________________\n")
        if g==0:
            print(f"{player_1} chose : "+rel_1+f"\n{player_2} chose :",rel_2,"\nIt was a DRAW!")
            draw+=1
        elif g==1:
            print(f"{player_1} chose : "+rel_1+f"\n{player_2} chose :",rel_2,f"\n{player_1} WINS!")
            win_1+=1
        elif g==-1:
            print(f"{player_1} chose : "+rel_1+f"\n{player_2} chose :",rel_2,f"\n{player_2} WINS!")
            win_2+=1
        print("__________________________________________\n\n")
        enter = input("Press 'Enter' to continue...")
        if enter=="":
            clear_output() #clearing outpurt over here![2]

    print("Games Played : ",rounds,"rounds")
    point_1="point" if win_1 ==1 else "points"
    point_2="point" if win_2 ==1 else "points"
    games_were_drawn="games were drawn." if draw>1 else "game was drawn!"
    print(f"{player_1} -> {win_1} {point_1}!")
    print(f"{player_2} -> {win_2} {point_2}!")
    print(draw,games_were_drawn)

    if win_1>win_2:
        print(f"{player_1} is the CHAMPION!!")
    elif win_2>win_1:
        print(f"{player_2} is the CHAMPION!!")
    else:
        print("It was a tie match!")
    
    with open("swg_logs.txt","a") as f:
        f.write(f"\n\n___Multiplayer___[{fullDate}]\n")
        f.write(f"{player_1} V/S {player_2}\n")
        f.write(f"Rounds played : {rounds}\n")
        f.write(f"{player_1}[Player one] win : {win_1}\n")
        f.write(f"{player_2}[Player two] win : {win_2}\n")
        f.write(f"Draw games : {draw}")
        


elif fi==1:
    player=input("Name : ")
    i=1
    while i!=rounds+1:
        options=["s","w","g"]
        rc=choice(options)
        sr=real(rc)
        print("\nRound",i,"\n"+"*"*i)
        uc=input("Type S for Snake, W for Water and G for Gun :>>> ").lower()
        f=swg(uc)
        if f==1:
            print("Invalid Input!\nTry again...")
            continue
        i+=1
        rel=real(uc)
        g=game(uc,rc)
        print("Waiting for machine.")
        sleep(0.33)
        print("Waiting for machine..")
        sleep(0.33)
        print("Waiting for machine...")
        sleep(0.33)


        if g==0:
            print("You chose : "+rel+"\nSystem chose :",sr,"\nIt was a DRAW!")
            draw+=1
        elif g==1:
            print("You chose : "+rel+"\nSystem chose :",sr,"\nYou WIN!")
            win+=1
        elif g==-1:
            print("You chose : "+rel+"\nSystem chose :",sr,"\nYou LOST!")
            lose+=1

    print(f"You_Played {rounds} games:\n_________________________________________\nLoses :{lose} \nWins : {win}\nDraws = {draw}")

    if win>lose:
        print("Congratulations!")
    else:
        print('Better luck next time <3')
        
    with open("swg_logs.txt","a") as f:
        f.write(f"\n\n___Player V/S Computer___{fullDate}\n")
        f.write(f"Player : {player}\n")
        f.write(f"{rounds} rounds played.\n")
        f.write(f"Player[{player}] win : {win}\n")
        f.write(f"System win :{lose}\n")
        f.write(f"Games drawn : {draw}\n")

        
