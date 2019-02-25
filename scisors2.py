
from random import randint


def rock():




    #create a list of play options
    #print("Type r for ROCK , p for PAPER , s for Scissors")
    t = ["Rock", "Paper", "Scissors"]

    #assign a random play to the computer
    computer = t[randint(0,2)]

    #set player to False
    #player = False
    
    #licznik gier
    how_many =[]
    

    #while player == False:
    #  gramy 3 tury
    while len(how_many) != 3:   

    #set player to True
        player = input("Rock, Paper, Scissors?").capitalize()
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                how_many.append("L")
                print(how_many) 
            else:
                print("You win!", player, "smashes", computer)
                how_many.append("W")
                print(how_many)

        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                how_many.append("L")
                print(how_many) 
            else:
                print("You win!", player, "covers", computer)
                how_many.append("W")
                print(how_many)

        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                how_many.append("L")
                print(how_many) 
            else:
                print("You win!", player, "cut", computer)
                how_many.append("W")
                print(how_many)

        else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        #player = False
        #rock()
        computer = t[randint(0,2)]
    
    
    if len(how_many)>=3:
        # sadze ze zamiiast ponizszego warunku powinien byc warunek choc jednej wygranej w 3 turach poniewaz teraz jest za ciezko wygrac [ how_many.count("W") >= 1 ]
        # mozna dopisac historie ze przeciwnik jest przekonany o swojej nieomylnosci i pojedyncza przegrana sprawia ze traci sens zycia XD
        if how_many.count("W") > how_many.count("L"):
            print("jestttttttttttttttttttt")
            #file = open("congrats.txt",'r') 
            #print (file.read())
            return True
        else:
            print("nieeeeeeeeeeeeee")
            #file = open("lose.txt",'r') 
            #print (file.read())
            return False                

    
    
rock()