#Rishabh Shah
#2016
#Card Dealer

#imports
import time
import random
import sys
import textwrap

#define
def blankLine():
	print " "
	
def wait(timeWait):
	time.sleep(timeWait)

def playAnotherTime():
	while True:
		playAgain = raw_input("Would you like to deal again? (yes/no): ").lower()
		if playAgain == "no" or playAgain == "n":
			wait(1)
			blankLine()
			print "Goodbye"
			wait(1)
			blankLine()
			sys.exit()
		if playAgain == "yes" or playAgain == "y":
			wait(1)
			blankLine()
			return
		if playAgain != "yes" or playAgain != "y" or playAgain != "no" or playAgain != "n":
			wait(1)
			blankLine()
			print "You entered something that does not compute. Please try again"
			blankLine()
			wait(1)
			
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#welcome
blankLine()
s = "Welcome to Rishabh's card dealer. Please type in all numerical answers as " + color.BOLD + color.RED + "digits" +color.END + " (eg. instead of fifty-two, type 52). The final hands will be dealt as text."
print textwrap.fill(s)
wait(1)
blankLine()

while True:
	#deck of cards in a list
	possible_cards = ['2 of diamonds', '3 of diamonds', '4 of diamonds', '5 of diamonds', \
					 '6 of diamonds', '7 of diamonds', '8 of diamonds', '9 of diamonds', \
					 '10 of diamonds', 'Jack of diamonds', 'Queen of diamonds', 'King of diamonds', \
					 'Ace of diamonds', '2 of hearts', '3 of hearts', '4 of hearts', '5 of hearts', \
					 '6 of hearts', '7 of hearts', '8 of hearts', '9 of hearts', \
					 '10 of hearts', 'Jack of hearts', 'Queen of hearts', 'King of hearts', \
					 'Ace of hearts', '2 of spades', '3 of spades', '4 of spades', \
					 '5 of spades', '6 of spades', '7 of spades', '8 of spades', \
					 '9 of spades', '10 of spades', 'Jack of spades', 'Queen of spades', \
		  		 	 'King of spades', 'Ace of spades', '2 of clubs', '3 of clubs', \
				 	 '4 of clubs', '5 of clubs', '6 of clubs', '7 of clubs', \
					 '8 of clubs', '9 of clubs', '10 of clubs', 'Jack of clubs', \
					 'Queen of clubs', 'King of clubs', 'Ace of clubs']
	#asking how many hands and cards in each hand
	while True:
		while True:
			handsAsked = raw_input("How many hands would you like?: ")
			try:
				int(handsAsked) +1
			except:
				blankLine()
				wait(1)
				print "You entered something that does not compute. Please try again."
				blankLine()
				wait(1)
			else:
				blankLine()
				wait(1)
				break

		while True:	
			cardsAsked = raw_input("How many cards per hand would you like?: ")
			try:
				int(cardsAsked) + 1
			except:
				blankLine()
				wait(1)
				print "You entered something that does not compute. Please try again."
				blankLine()
				wait(1)
			else:
				blankLine()
				wait(1)
				break
						
		if int(handsAsked)*int(cardsAsked) > 52:
			print "You entered something that does not compute. Please try again"
			continue
		else:
			break

	#dealing the cards and creating the lists
	handNumber = 1
	for i in range(int(handsAsked)):
		tableRow = []
		for i in range(int(cardsAsked)):
			cardSelected = str(random.choice(possible_cards))
			possible_cards.remove(str(cardSelected))
			tableRow.append(cardSelected)
		t = "Hand " + str(handNumber) + ": " + ", ".join(tableRow)
		print textwrap.fill(t)
		blankLine()
		handNumber += 1

	#playing agian
	blankLine()
	wait(1)
	playAnotherTime()
