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
			print "You entered something that doesn't exist. Please try again"
			print " "
			wait(1)
			
def blankLine():
	print " "

#defining varibles
##possible_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
##possible_suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
possible_cards = ['2 of diamonds', '3 of diamonds', '4 of diamonds', '5 of diamonds', '6 of diamonds', '7 of diamonds', '8 of diamonds', '9 of diamonds', '10 of diamonds', 'Jack of diamonds', 'Queen of diamonds', 'King of diamonds', 'Ace of diamonds', '2 of hearts', '3 of hearts', '4 of hearts', '5 of hearts', '6 of hearts', '7 of hearts', '8 of hearts', '9 of hearts', '10 of hearts', 'Jack of hearts', 'Queen of hearts', 'King of hearts', 'Ace of hearts', '2 of spades', '3 of spades', '4 of spades', '5 of spades', '6 of spades', '7 of spades', '8 of spades', '9 of spades', '10 of spades', 'Jack of spades', 'Queen of spades', 'King of spades', 'Ace of spades', '2 of clubs', '3 of clubs', '4 of clubs', '5 of clubs', '6 of clubs', '7 of clubs', '8 of clubs', '9 of clubs', '10 of clubs', 'Jack of clubs', 'Queen of clubs', 'King of clubs', 'Ace of clubs']

while True:
	blankLine()
	playerCard1 = str(random.choice(possible_cards))
	print "You were dealed the "+ playerCard1 +"."
	wait(1)
	blankLine()
	dealerCard1 = str(random.choice(possible_cards))
	print "The dealer was dealed the "+ dealerCard1 +"."
	wait(1)
	blankLine()
	playerCard2 = str(random.choice(possible_cards))
	print "You were dealed the "+ playerCard2 +"."
	wait(1)
	blankLine()
	dealerCard2 = str(random.choice(possible_cards))
	print "The dealer was dealed the "+ dealerCard2 +"."
	wait(1)
	blankLine()
	#scoring
	playerCount = 0
	dealerCount = 0
	if "2" in playerCard1:
		playerCount += 2
	elif "3" in playerCard1:
		playerCount += 3
	elif "4" in playerCard1:
		playerCount += 4
	elif "5" in playerCard1:
		playerCount += 5
	elif "6" in playerCard1:
		playerCount += 6
	elif "7" in playerCard1:
		playerCount += 7
	elif "8" in playerCard1:
		playerCount += 8
	elif "9" in playerCard1:
		playerCount += 9
	elif "10" in playerCard1:
		playerCount += 10
	elif "Jack" in playerCard1:
		playerCount += 10
	elif "Queen" in playerCard1:
		playerCount += 10
	elif "King" in playerCard1:
		playerCount += 10
	elif "Ace" in playerCard1:
		playerCount += 11
	if "2" in playerCard2:
		playerCount += 2
	elif "3" in playerCard2:
		playerCount += 3
	elif "4" in playerCard2:
		playerCount += 4
	elif "5" in playerCard2:
		playerCount += 5
	elif "6" in playerCard2:
		playerCount += 6
	elif "7" in playerCard2:
		playerCount += 7
	elif "8" in playerCard2:
		playerCount += 8
	elif "9" in playerCard2:
		playerCount += 9
	elif "10" in playerCard2:
		playerCount += 10
	elif "Jack" in playerCard2:
		playerCount += 10
	elif "Queen" in playerCard2:
		playerCount += 10
	elif "King" in playerCard2:
		playerCount += 10
	elif "Ace" in playerCard2:
		playerCount += 11
	if "2" in dealerCard1:
		dealerCount += 2
	elif "3" in dealerCard1:
		dealerCount += 3
	elif "4" in dealerCard1:
		dealerCount += 4
	elif "5" in dealerCard1:
		dealerCount += 5
	elif "6" in dealerCard1:
		dealerCount += 6
	elif "7" in dealerCard1:
		dealerCount += 7
	elif "8" in dealerCard1:
		dealerCount += 8
	elif "9" in dealerCard1:
		dealerCount += 9
	elif "10" in dealerCard1:
		dealerCount += 10
	elif "Jack" in dealerCard1:
		dealerCount += 10
	elif "Queen" in dealerCard1:
		dealerCount += 10
	elif "King" in dealerCard1:
		dealerCount += 10
	elif "Ace" in dealerCard1:
		dealerCount += 11
	if "2" in dealerCard2:
		dealerCount += 2
	elif "3" in dealerCard2:
		dealerCount += 3
	elif "4" in dealerCard2:
		dealerCount += 4
	elif "5" in dealerCard2:
		dealerCount += 5
	elif "6" in dealerCard2:
		dealerCount += 6
	elif "7" in dealerCard2:
		dealerCount += 7
	elif "8" in dealerCard2:
		dealerCount += 8
	elif "9" in dealerCard2:
		dealerCount += 9
	elif "10" in dealerCard2:
		dealerCount += 10
	elif "Jack" in dealerCard2:
		dealerCount += 10
	elif "Queen" in dealerCard2:
		dealerCount += 10
	elif "King" in dealerCard2:
		dealerCount += 10
	elif "Ace" in dealerCard2:
		dealerCount += 11
	print "player count is " + str(playerCount)
	print "dealer count is " + str(dealerCount)
	playAnotherTime()
