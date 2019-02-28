import os
import rogal
import highstore
from timeit import default_timer as timer

def main_menu():

    file = open("/home/szymon/codecool/PYTHON/roguelike_v2/ascii_art/castle1.txt",'r') 
    print(file.read())

    print("""
    1.create character and start a game
    2.highscores
    3.how to play
    4.authors
    5.exit""")

    choice = input("Type a number: ")

    if choice == '1':
        rogal.add_character_stats()
        rogal.get_player_position()
        # start = timer()
        rogal.controls()
        # end = timer()
        # game_time = end - start
        # highstore.print_score(rogal.stats, game_time)

    if choice == '2':
        pass

    if choice == '3':
        file = open("ascii_art/howtoplay.txt",'r')
        print(file.read())

        back = input("press anything to go back to main menu")
        if len(back)>0:
            main_menu()

    if choice == '4':
        file = open("/home/szymon/codecool/PYTHON/roguelike_v2/ascii_art/Authors.txt", 'r')
        print(file.read())
        file.close()
        back = input("press anything to go back to main menu")
        main_menu()

    if choice == '5':
        quit()


def main():
    main_menu()


if __name__ == "__main__":
    main()
