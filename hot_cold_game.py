import random
def hotcold():
    print("type a number ".upper())

    numbers = random.randint(1,100)
    #print(numbers)
    answer = 0
    listt = []
    while answer != numbers:
        try:
            answer = int(input("type a number:"))
            listt.append(answer)
            if answer == numbers:
                file = open("/home/szymon/codecool/PYTHON/roguelike_v2/ascii_art/congrats.txt", 'r')
                print(file.read())
                file.close()
            elif answer < numbers:
                print("type bigger number")
            elif answer > numbers:
                print("type smaller number")
        except ValueError:
            print("type number , not letter")
        if len(listt) == 20:
            print("loser hahahah")
            break
