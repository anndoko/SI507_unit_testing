import random
import unittest

# SI 507 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: SI507-008 Mo 1:00PM - 2:30PM
# People you worked with: No

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p1 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################


### Write unit tests below this line for the cards code above.
# PART 1.
class TestCard(unittest.TestCase):

	# this is a "test"
	def test_create(self):
		card = Card()
		self.assertEqual(self.card1.suit, "Diamonds")
		self.assertEqual(self.card1.rank, 3)

	# Test that if you create a card with rank 12, its rank will be "Queen"
	def testCreateQueen(self):
		card = Card(rank = 12)
		self.assertEqual(card.rank, "Queen")

	# Test that if you create a card with rank 1, its rank will be "Ace"
	def testCreateAce(self):
		card = Card(rank = 1)
		self.assertEqual(card.rank, "Ace")

	# Test that if you create a card instance with rank 3, its rank will be 3
	def testCreateRank3(self):
		card = Card(rank = 3)
		self.assertEqual(card.rank, 3)

	# Test that if you create a card instance with suit 1, it will be suit "Clubs"
	def testCreateSuitClubs(self):
		card = Card(suit = 1)
		self.assertEqual(card.suit, "Clubs")

	# Test that if you create a card instance with suit 2, it will be suit "Hearts"
	def testCreateSuitHearts(self):
		card = Card(suit = 2)
		self.assertEqual(card.suit, "Hearts")

	# Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	def testSuitNames(self):
		card = Card()
		self.assertEqual(card.suit_names, ["Diamonds","Clubs","Hearts","Spades"])

	# Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"
	def testCardString1(self):
		card = Card(suit = 2, rank = 7)
		self.assertEqual(card.__str__(), "7 of Hearts")

	# Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"
	def testCardString2(self):
		card = Card(suit = 3, rank = 13)
		self.assertEqual(card.__str__(), "King of Spades")

	# Test that if you create a deck instance, it will have 52 cards in its cards instance variable
	def testDeckCards(self):
		deck = Deck()
		self.assertEqual(len(deck.cards), 52)

	# Test that if you invoke the pop_card method on a deck, it will return a card instance.
	def testPopCardInstance(self):
		deck = Deck()
		card = deck.pop_card()
		self.assertIsInstance(card, Card)

	# Test that if you invoke the pop_card method on a deck, the deck has one fewer cards in it afterwards.
	def testPopCardFewer(self):
		deck = Deck()
		deck.pop_card()
		self.assertLess(len(deck.cards), 52)

	# Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. (This will probably require multiple assertions!)
	def testReturnValue(self):
		return_value = play_war_game()
		self.assertEqual = (type(return_value), tuple)
		self.assertEqual = (len(return_value), 3)
		self.assertEqual = (type(return_value[0]), str)

	# (and 14)  Write at least 2 additional tests (not repeats of the above described tests). Make sure to include a descriptive message in these two so we can easily see what you are testing!
	def test(self):
		pass

# PART 2:
class Hand:
	# create the Hand with an initial set of cards
	# param: a list of cards
	def __init__(self, init_cards):
		self.cards = []
		for card in init_cards:
			self.cards.append(card)

	# add a card to the hand
	# silently fails if the card is already in the hand
	# param: the card to add
	# returns: nothing
	def add_card(self, card):
		if card not in self.cards:
			self.cards.append(card)

	# remove a card from the hand
	# param: the card to remove
	# returns: the card, or None if the card was not in the Hand
	def remove_card(self, card):
		if card in self.cards:
			self.cards.remove(card)
			return card
		else:
			return None
	# draw a card from a deck and add it to the hand
	# side effect: the deck will be depleted by one card
	# param: the deck from which to draw
	# returns: nothing
	def draw(self, deck):
		card = deck.pop_card()
		self.cards.append(card)

class TestHand(unittest.TestCase):

	# Test that a hand is initialized properly.
	def testHandInit(self):
		pass

	# Test that add_card( ) and remove_card( ) behave as specified
	def testAddAndRemove(self):
		pass

	# Test that draw( ) works as specified. Test side effects as well.
	def testDraw(self):
		pass


#############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
