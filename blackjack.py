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

		print "The player's cards are: " + ", ".join(player_cards)
		print "The dealer's cards are: " + ", ".join(dealer_cards)
		blankLine()

		player_count = 0
		dealer_count = 0

		list_item = 0
		for item in player_cards:
			if "2" in player_cards[list_item]:
				player_count += 2
			elif "3" in player_cards[list_item]:
				player_count += 3
			elif "4" in player_cards[list_item]:
				player_count += 4
			elif "5" in player_cards[list_item]:
				player_count += 5
			elif "6" in player_cards[list_item]:
				player_count += 6
			elif "7" in player_cards[list_item]:
				player_count += 7
			elif "8" in player_cards[list_item]:
				player_count += 8
			elif "9" in player_cards[list_item]:
				player_count += 9
			elif "10" in player_cards[list_item]:
				player_count += 10
			elif "Jack" in player_cards[list_item]:
				player_count += 10
			elif "Queen" in player_cards[list_item]:
				player_count += 10
			elif "King" in player_cards[list_item]:
				player_count += 10
			elif "Ace" in player_cards[list_item]:
				player_count += 11

			list_item +=1

		list_item = 0	
		for item in dealer_cards:
			if "2" in dealer_cards[list_item]:
				dealer_count += 2
			elif "3" in dealer_cards[list_item]:
				dealer_count += 3
			elif "4" in dealer_cards[list_item]:
				dealer_count += 4
			elif "5" in dealer_cards[list_item]:
				dealer_count += 5
			elif "6" in dealer_cards[list_item]:
				dealer_count += 6
			elif "7" in dealer_cards[list_item]:
				dealer_count += 7
			elif "8" in dealer_cards[list_item]:
				dealer_count += 8
			elif "9" in dealer_cards[list_item]:
				dealer_count += 9
			elif "10" in dealer_cards[list_item]:
				dealer_count += 10
			elif "Jack" in dealer_cards[list_item]:
				dealer_count += 10
			elif "Queen" in dealer_cards[list_item]:
				dealer_count += 10
			elif "King" in dealer_cards[list_item]:
				dealer_count += 10
			elif "Ace" in dealer_cards[list_item]:
				dealer_count += 11

			list_item +=1

		print "The player count is " + str(player_count)
		print "The dealer count is " + str(dealer_count)
		blankLine()

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
			list_item = 0
			dealer_count = 0
			for item in dealer_cards:
				if "2" in dealer_cards[list_item]:
					dealer_count += 2
				elif "3" in dealer_cards[list_item]:
					dealer_count += 3
				elif "4" in dealer_cards[list_item]:
					dealer_count += 4
				elif "5" in dealer_cards[list_item]:
					dealer_count += 5
				elif "6" in dealer_cards[list_item]:
					dealer_count += 6
				elif "7" in dealer_cards[list_item]:
					dealer_count += 7
				elif "8" in dealer_cards[list_item]:
					dealer_count += 8
				elif "9" in dealer_cards[list_item]:
					dealer_count += 9
				elif "10" in dealer_cards[list_item]:
					dealer_count += 10
				elif "Jack" in dealer_cards[list_item]:
					dealer_count += 10
				elif "Queen" in dealer_cards[list_item]:
					dealer_count += 10
				elif "King" in dealer_cards[list_item]:
					dealer_count += 10
				elif "Ace" in dealer_cards[list_item]:
					dealer_count += 11
				list_item +=1

			print "The player count is " + str(player_count)
			print "The dealer count is " + str(dealer_count)
			blankLine()

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
				dealAgain = raw_input("Would you like another hand?: ")
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
			print "The player's cards are: " + ", ".join(player_cards)
			blankLine()

			list_item = 0
			player_count = 0
			for item in player_cards:
				if "2" in player_cards[list_item]:
					player_count += 2
				elif "3" in player_cards[list_item]:
					player_count += 3
				elif "4" in player_cards[list_item]:
					player_count += 4
				elif "5" in player_cards[list_item]:
					player_count += 5
				elif "6" in player_cards[list_item]:
					player_count += 6
				elif "7" in player_cards[list_item]:
					player_count += 7
				elif "8" in player_cards[list_item]:
					player_count += 8
				elif "9" in player_cards[list_item]:
					player_count += 9
				elif "10" in player_cards[list_item]:
					player_count += 10
				elif "Jack" in player_cards[list_item]:
					player_count += 10
				elif "Queen" in player_cards[list_item]:
					player_count += 10
				elif "King" in player_cards[list_item]:
					player_count += 10
				elif "Ace" in player_cards[list_item]:
					player_count += 11
				list_item +=1
			
			print "The player count is " + str(player_count)
			print "The dealer count is " + str(dealer_count)
			blankLine()

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