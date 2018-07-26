#игра виселица
import random
my_list=['france','belgium','usa','russia','spain','england','finland',
'estonia','ukraine','georgia','germany','brasil','argentina','poland']
word=random.choice(my_list)
def hangman(word):
	wrong=0#переменнная непарвильных предположений
	stages=["",
			"________         ",
			"|                ",
			"|       |        ",
			"|       0        ",
			"|     / | \      ",
			"|      / \       ",
			"|                ",
			]
	rletters = list(word)#список правильных букв
	board = ["__"] * len(word)#переменная списка строк для отгадывания
	win=False#переменная для отслеживания победы
	print("Let's guess the country !")
	print("Welcome to execution!")
	while wrong<len(stages)-1:	 
		print("\n")#
		msg="Enter the letter:   "
		char=input(msg)#введенное игроком
		if char in rletters:
			cind=rletters.index(char)#
			board[cind]=char#
			rletters[cind]="$"#
		else:
			wrong+=1#
		print((" ".join(board)))#
		e=wrong+1#
		print("\n".join(stages[0:e]))#
		if "__" not in board:#
			print("You win ! The word  was: ",word)
			print(" ".join(board))#
			win = True
			break
	if not win:#	       		
		print("\n".join(stages[0:wrong]))
		print("You lose ! The word was: {}.".format(word))									
hangman(word)			
					          	 
	
