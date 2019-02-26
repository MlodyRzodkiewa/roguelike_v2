import os
import random
import platform
import items
import scisors2

try:
	from msvcrt import getch 
except ImportError:

	def getch():

		import sys
		import tty
		import termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch


def pressedkey():
	return getch()

	
		  # 0   1   2   3   4   5   6   7   8   9  10   11  12  13  14  15  16  17  18  19  20  21  22  23 
room = {1:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'], # ^
		2:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		3:['#','.','.','.','.','.','.','.','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		4:['#','.','.','.','.','.','.','#','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		5:['#','.','.','.','.','.','@','#','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		6:['#','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','C','.','.','#'], # |
		7:['#','.','.','.','.','#','#','#','.','#','#','C','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		8:['#','.','.','.','.','.','.','.','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','#'], # |
		9:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
		10:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],# |
		11:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','#','#','#','#','#','#','#'],# x
		12:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		13:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		14:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		15:['#','.','.','.','.','.','.','.','$','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		16:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','1','.','.','#'],# |
		17:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		18:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		19:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
		20:['#','.','$','.','.','.','.','.','.','.','.','.','.','.','.','#','A','.','.','.','.','.','.','#'],# |
		21:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#'],# |
	    22:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']}# |
		# <--------------------------------------------y------------------------------------------------------->
actors = {'wall'  :  "#",
		  'player':  "@",
		  'empty' :  ".",
		  'money' :  "$",
		  'chest' :  "C"}
stats = {'hp': 10,'exp': 0,'def': 1,'atc': 1,'lvl': 1}


inventory = []
otherlist = []
pos = [] 

def pick_up():
#	for key in room:
#		print(room[key])# ta linijka wyswietla duza mape XD

	if pos == [20, 2] and 'melon' in otherlist:
		print()
	elif pos == [20, 2] and 'melon' not in otherlist:
		otherlist.append('melon')
		inventory.append('hp')
		inventory.append('hp')
		add_to_inventory(stats, inventory)
		print("added hp")
		inventory.clear()

	if pos == [15, 8] and 'plum' in otherlist:
		print()
	elif pos == [15, 8] and 'plum' not in otherlist:
		otherlist.append('plum')
		inventory.append('hp')
		add_to_inventory(stats, inventory)
		print("added hp")
		inventory.pop()

	if pos == [6, 20] and 'leather gloves' in otherlist:
		print()
	elif pos == [6, 20] and 'leather gloves' not in otherlist:
		otherlist.append('leather gloves')
		inventory.append('def')
		add_to_inventory(stats, inventory)
		print("added def")
		inventory.pop()

	if pos == [7, 11] and 'Greater kahoot armor' in otherlist:
		print()
	elif pos == [7, 11] and 'Greater kahoot armor' not in otherlist:
		otherlist.append('Greater kahoot armor')
		inventory.append('def')
		inventory.append('def')
		add_to_inventory(stats, inventory)
		print("added def")
		inventory.clear()
	
#################3
	# TODO poprwić trza
	for item in items.clothes():
		if pos == [20, 16] and item in item.clothes() in otherlist:
			print()
		elif pos == [20, 16] and items.clothes() not in otherlist:
			otherlist.append(items.clothes()[random.randint(0, len(items.clothes())-1)])
			inventory.append('atc')
			inventory.append('atc')
			add_to_inventory(stats, inventory)
			print("added atc")
			inventory.clear()				
#################

	if pos == [16, 20] and 'Nazgûl' in otherlist:
		print()
	elif pos == [16, 20] and 'Nazgûl' not in otherlist:
		otherlist.append('Nazgûl')
		scisors2.rock()
		inventory.append('exp')
		add_to_inventory(stats, inventory)
		inventory.clear()


################################################################################
################################################################################


def add_to_inventory(inventory, added_items):
	for item in added_items:
		inventory.setdefault(item, 0)
		inventory[item] += 1
	#print()
	#print(inventory)
	return inventory


############################################################################################################
##########################################################################################################
#########################################################################################################
def gamemap():
	for i in range(1,len(room)+1):
		print("".join(room[i]))

def player_pos():
	for i in range(1,len(room)+1):
		if actors['player'] in room[i]:
			x_axis = i
			y_axis = room[i].index(actors['player'])
			global pos
			del pos[:]
			pos.append(x_axis)
			pos.append(y_axis)

def updater():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear')
	gamemap()
	player_pos()
	pick_up()
	print(inventory)
	print(stats)
	print(otherlist)
 

def up(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]-1]).pop(pos[1])
	(ditcioary[pos[0]-1]).insert(pos[1],inst_player)


def down(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]+1]).pop(pos[1])
	(ditcioary[pos[0]+1]).insert(pos[1],inst_player)


def left(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]]).pop(pos[1]-1)
	(ditcioary[pos[0]]).insert(pos[1]-1,inst_player)


def right(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]]).pop(pos[1]+1)
	(ditcioary[pos[0]]).insert(pos[1]+1,inst_player)



def controls():
	while True:
		pressedkey = getch()
		if pressedkey is 'w' or pressedkey is 'W':
			if room[pos[0]-1][pos[1]] is not actors['wall']:
				up(room, actors['empty'], actors['player'])
				updater()
				print(pos)
		elif pressedkey is 's' or pressedkey is 'S':
			if room[pos[0]+1][pos[1]] is not actors['wall']:
				down(room,actors['empty'],actors['player'])
				updater()
				print(pos)
		elif pressedkey is 'a' or pressedkey is 'A':
			if room[pos[0]][pos[1]-1] is not actors['wall']:
				left(room,actors['empty'], actors['player'])
				updater()
				print(pos)
		elif pressedkey is 'd' or pressedkey is 'D':
			if room[pos[0]][pos[1]+1] is not actors['wall']:
				right(room,actors['empty'], actors['player'])
				updater()
				print(pos)


#updater()

##############################################################################################
##############################################################################################


def print_character_statistics(char_stats):
    string = "hp:{:}\tdef:{:}\tatc:{:}\texp:{:}\tlvl:{:}"
    print(string.format(*char_stats.values()))

def add_character_stats():
	print_character_statistics(stats)
	points = 5
	while points > 0:
		#while not is_answer_correct:
		stat_to_add = input("Enter 'H', 'h', 'D', 'd' or 'A', 'a' to add statistic: ")
		if stat_to_add in ["h", "H"]:
			stats["hp"] += 2
		elif stat_to_add in ["D", "d"]:
			stats["def"] += 1
		elif stat_to_add in ["A", "a"]:
			stats["atc"] += 1
		points -= 1
		os.system("clear")
		print_character_statistics(stats)


add_character_stats()
player_pos()
controls()
