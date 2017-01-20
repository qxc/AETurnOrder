import random
import sys

turnDiscard = []

def setPlayerCount():
        global turnDeck
        numPlayers = input("How many players are you playing with? (1,2,3,4) ")
        if numPlayers == str(1):
                turnDeck = ["p1","p1","p1","nemesis","nemesis"]
        if numPlayers == str(2):
                turnDeck = ["p1", "p2", "p1", "p2", "nemesis", "nemesis"]
        if numPlayers == str(3):
                turnDeck = ["p1", "p2", "p3", "wildcard", "nemesis", "nemesis"]
        if numPlayers == str(4):
                turnDeck = ["p1", "p2", "p3", "p4", "nemesis", "nemesis"]        

def shuffle():
	random.shuffle(turnDeck)

def takeTurn():
	print(turnDeck[0])
	turnDiscard.append(turnDeck.pop(0))

def fullRound():
        while len(turnDeck) > 0:
                takeTurn()
                input("Press enter for next turn")
        
def resetDeck():
        while len(turnDiscard) > 0:
                turnDeck.append(turnDiscard.pop(0))
        shuffle()

def game():
        roundNum = 0
        while(True):
                shuffle()
                fullRound()
                roundNum = roundNum+1
                print("\n****Current round: " + str(roundNum) + "****")
                resetDeck()

setPlayerCount()
game()

