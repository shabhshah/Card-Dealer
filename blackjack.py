# Rishabh Shah
# 2015
# Python Black Jack game

#imports
import time
import random
import sys

#define
def wait(timeWait):
	time.sleep(timeWait)

def playAnotherTime():
	blankLine()
	while True:
		playAgain = raw_input("Would you like to play again? (yes/no): ").lower()
		if playAgain == "no" or playAgain == "n":
			wait(1)
			print " "		
			print "Goodbye"
			wait(1)
			print " "
			sys.exit()
		if playAgain == "yes" or playAgain == "y":
			wait(1)
			return
			print " "
		if playAgain != "yes" or "y" or "no" or "n":
			wait(1)
			print " "
			print "You entered something that does not compute. Please try again"
			print " "
			wait(1)
			
def blankLine():
	print " "

def playerCount(x,y):
	list_item = 0
	for item in y:
		if "2" in y[list_item]:
			x += 2
		elif "3" in y[list_item]:
			x += 3
		elif "4" in y[list_item]:
			x += 4
		elif "5" in y[list_item]:
			x += 5
		elif "6" in y[list_item]:
			x += 6
		elif "7" in y[list_item]:
			x += 7
		elif "8" in y[list_item]:
			x += 8
		elif "9" in y[list_item]:
			x += 9
		elif "10" in y[list_item]:
			x += 10
		elif "Jack" in y[list_item]:
			x += 10
		elif "Queen" in y[list_item]:
			x += 10
		elif "King" in y[list_item]:
			x += 10
		elif "Ace" in y[list_item]:
			x += 11
		list_item +=1

def score():
	global player_count
	global dealer_count
	print "The player count is " + str(player_count)
	print "The dealer count is " + str(dealer_count)
	blankLine()


while True:
	while True:
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
		player_cards = []
		dealer_cards = []
		ifcont = 100000
		blankLine()

		for i in xrange(0,2):
			player_card = random.choice(possible_cards)
			possible_cards.remove(player_card)
			player_cards.append(player_card)
			dealer_card = random.choice(possible_cards)
			possible_cards.remove(dealer_card)
			dealer_cards.append(dealer_card)

		print "The dealer's cards are: " + ", ".join(dealer_cards)
		print "Your cards are: " + ", ".join(player_cards)
		blankLine()

		playerCount(player_count,player_cards)
		playerCount(dealer_count,dealer_cards)
		score()

		if player_count == 21:
			print "You win!"
			break

		elif dealer_count == 21:
			print "The dealer wins!"
			break

		elif player_count > 21:
			print "The dealer wins!"
			break

		elif dealer_count > 21:
			print "You win!"
			break

		else:
			pass

		while dealer_count < 17:
			dealer_card = random.choice(possible_cards)
			possible_cards.remove(dealer_card)
			dealer_cards.append(dealer_card)		
			print "The dealer's cards are: " + ", ".join(dealer_cards)
			blankLine()
		
			playerCount(dealer_count,dealer_cards)

			score()

			if player_count == 21:
				print "You win!"
				break

			elif dealer_count == 21:
				print "The dealer wins!"
				ifcont = 0
				break

			elif player_count > 21:
				print "The dealer wins!"
				break

			elif dealer_count > 21:
				print "You win!"
				ifcont = 0
				break

			else:
				pass

		if ifcont == 0:
			break

		while True:

			while True:
				dealAgain = raw_input("Would you like another card?: ")
				if dealAgain == "yes" or \
				   dealAgain == "y":
					ifcont = 1
					break
				if dealAgain == "no" or \
				   dealAgain == "n":
					ifcont = 0
					break
				if dealAgain != "yes" or \
				   dealAgain != "y" or \
				   dealAgain != "no" or \
				   dealAgain != "n":
					print "You entered something that does not compute. Please try again."
			if ifcont == 0:
				break
			blankLine()
			player_card = random.choice(possible_cards)
			possible_cards.remove(player_card)
			player_cards.append(player_card)
			print "Your cards are: " + ", ".join(player_cards)
			blankLine()

			playerCount(player_count,player_cards)
			
			score()

			if player_count == 21:
				print "You win!"
				ifcont = 0
				break

			elif dealer_count == 21:
				print "The dealer wins!"
				ifcont = 0
				break

			elif player_count > 21:
				print "The dealer wins!"
				ifcont = 0
				break

			elif dealer_count > 21:
				print "You win!"
				ifcont = 0
				break

			else:
				ifcont = 1

		if ifcont == 0:
			break
		
		if dealer_count > player_count:
			print "The dealer wins!"
			break

		if dealer_count < player_count:
			print "You win!"
			break

	playAnotherTime()