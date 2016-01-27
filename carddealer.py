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
s = "Welcome to Rishabh's card dealer. Please type in all numerical answers as " + color.BOLD + "digits" +color.END + " (eg. instead of fifty-two, type 52). The final hands will be dealt into a table."
print textwrap.fill(s)
wait(1)
blankLine()

while True:
	#deck of cards in a list
	possible_cards = ['2 of diamonds', '3 of diamonds', '4 of diamonds', '5 of diamonds', '6 of diamonds', '7 of diamonds', '8 of diamonds', '9 of diamonds', '10 of diamonds', 'Jack of diamonds', 'Queen of diamonds', 'King of diamonds', 'Ace of diamonds', '2 of hearts', '3 of hearts', '4 of hearts', '5 of hearts', '6 of hearts', '7 of hearts', '8 of hearts', '9 of hearts', '10 of hearts', 'Jack of hearts', 'Queen of hearts', 'King of hearts', 'Ace of hearts', '2 of spades', '3 of spades', '4 of spades', '5 of spades', '6 of spades', '7 of spades', '8 of spades', '9 of spades', '10 of spades', 'Jack of spades', 'Queen of spades', 'King of spades', 'Ace of spades', '2 of clubs', '3 of clubs', '4 of clubs', '5 of clubs', '6 of clubs', '7 of clubs', '8 of clubs', '9 of clubs', '10 of clubs', 'Jack of clubs', 'Queen of clubs', 'King of clubs', 'Ace of clubs']
	#asking how many hands and cards in each hand
	while True:
		while True:
			handsAsked = raw_input("How many hands would you like?: ")
			if str(handsAsked) == '52' or str(handsAsked) == '51' or str(handsAsked) == '50' or str(handsAsked) == '49' or str(handsAsked) == '48' or str(handsAsked) == '47' or str(handsAsked) == '46' or str(handsAsked) == '45' or str(handsAsked) == '44' or str(handsAsked) == '43' or str(handsAsked) == '42' or str(handsAsked) == '41' or str(handsAsked) == '40' or str(handsAsked) == '39' or str(handsAsked) == '38' or str(handsAsked) == '37' or str(handsAsked) == '36' or str(handsAsked) == '35' or str(handsAsked) == '34' or str(handsAsked) == '33' or str(handsAsked) == '32' or str(handsAsked) == '31' or str(handsAsked) == '30' or str(handsAsked) == '29' or str(handsAsked) == '28' or str(handsAsked) == '27' or str(handsAsked) == '26' or str(handsAsked) == '25' or str(handsAsked) == '24' or str(handsAsked) == '23' or str(handsAsked) == '22' or str(handsAsked) == '21' or str(handsAsked) == '20' or str(handsAsked) == '19' or str(handsAsked) == '18' or str(handsAsked) == '17' or str(handsAsked) == '16' or str(handsAsked) == '15' or str(handsAsked) == '14' or str(handsAsked) == '13' or str(handsAsked) == '12' or str(handsAsked) == '11' or str(handsAsked) == '10' or str(handsAsked) == '9' or str(handsAsked) == '8' or str(handsAsked) == '7' or str(handsAsked) == '6' or str(handsAsked) == '5' or str(handsAsked) == '4' or str(handsAsked) == '3' or str(handsAsked) == '2' or str(handsAsked) == '1':
				blankLine()
				wait(1)
				break
			else:
				blankLine()
				wait(1)
				print "You entered something that does not compute. Please try again."
				blankLine()
				wait(1)
				continue

		while True:	
			cardsAsked = raw_input("How many cards per hand would you like?: ")
			if str(cardsAsked) == '52' or str(cardsAsked) == '51' or str(cardsAsked) == '50' or str(cardsAsked) == '49' or str(cardsAsked) == '48' or str(cardsAsked) == '47' or str(cardsAsked) == '46' or str(cardsAsked) == '45' or str(cardsAsked) == '44' or str(cardsAsked) == '43' or str(cardsAsked) == '42' or str(cardsAsked) == '41' or str(cardsAsked) == '40' or str(cardsAsked) == '39' or str(cardsAsked) == '38' or str(cardsAsked) == '37' or str(cardsAsked) == '36' or str(cardsAsked) == '35' or str(cardsAsked) == '34' or str(cardsAsked) == '33' or str(cardsAsked) == '32' or str(cardsAsked) == '31' or str(cardsAsked) == '30' or str(cardsAsked) == '29' or str(cardsAsked) == '28' or str(cardsAsked) == '27' or str(cardsAsked) == '26' or str(cardsAsked) == '25' or str(cardsAsked) == '24' or str(cardsAsked) == '23' or str(cardsAsked) == '22' or str(cardsAsked) == '21' or str(cardsAsked) == '20' or str(cardsAsked) == '19' or str(cardsAsked) == '18' or str(cardsAsked) == '17' or str(cardsAsked) == '16' or str(cardsAsked) == '15' or str(cardsAsked) == '14' or str(cardsAsked) == '13' or str(cardsAsked) == '12' or str(cardsAsked) == '11' or str(cardsAsked) == '10' or str(cardsAsked) == '9' or str(cardsAsked) == '8' or str(cardsAsked) == '7' or str(cardsAsked) == '6' or str(cardsAsked) == '5' or str(cardsAsked) == '4' or str(cardsAsked) == '3' or str(cardsAsked) == '2' or str(cardsAsked) == '1':
				blankLine()
				wait(1)
				break
			else:
				blankLine()
				wait(1)
				print "You entered something that does not compute. Please try again."
				blankLine()
				wait(1)
				continue
						
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
		handNumber += 1

	#playing agian
	blankLine()
	wait(1)
	playAnotherTime()
