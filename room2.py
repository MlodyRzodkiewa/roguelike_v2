
		  # 0   1   2   3   4   5   6   7   8   9  10   11  12  13  14  15  16  17  18  19  20  21  22  23 
room = {1:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'], # ^
		2:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		3:['#','.','.','.','.','.','.','.','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		4:['#','.','.','.','.','.','.','#','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		5:['#','.','.','.','.','.','@','#','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		6:['#','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','C','.','.','#'], # x
		7:['#','.','.','.','.','#','#','#','.','#','#','.','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		8:['#','.','.','.','.','.','.','.','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','#'],
		9:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		10:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
		11:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','#','#','#','#','#','#','#'],
		12:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
		13:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
		14:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
		15:['#','.','.','.','.','.','.','.','$','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
		16:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
		17:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
		18:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'], # |
		19:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
		20:['#','.','$','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
		21:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],
	    22:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']} 


# TO DZIALA
potion = {'hp': 10,'xp': 0,'def': 1,'atc':1}

def get_string_input(question):
    answer = input(question)

    return answer

def create_characterdef():
    points = 5
    while points > 0:
        #while not is_answer_correct:
        stat_to_add = get_string_input("Enter 'H', 'h', 'D', 'd' or 'A', 'a' to add statistic: ")
        if stat_to_add in ["h", "H"]:
            potion["hp"] += 2
        elif stat_to_add in ["D", "d"]:
            potion["def"] += 1
        elif stat_to_add in ["A", "a"]:
            potion["atc"] += 1
        points -= 1
    print('x')


create_characterdef()
print(potion)
