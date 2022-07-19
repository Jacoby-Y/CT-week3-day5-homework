import random


def card_value(num):
	if num <= 10:
		return num
	return 10

def val_to_str(val):
	if val == 1:
		return "Ace"
	elif val == 11:
		return "Jack"
	elif val == 12:
		return "Queen"
	elif val == 13:
		return "King"
	return str(val)

class Card:
	def __init__(self, num, suit):
		self.hidden = False
		self.num = num
		self.value = card_value(num)
		self.suit = suit
	def __str__(self):
		return f"{val_to_str(self.num)}{self.suit}" if not self.hidden else "??"
	def __repr__(self):
		return self.__str__()
	def __eq__(self, other):
		if not isinstance(other, Card):
			return False
		return self.__str__() == other.__str__()

class Deck:
	def __init__(self, cards: list[Card]):
		self.cards = cards
	def rand_card(self):
		return random.choice(self.cards)
	def remove_index(self, index):
		self.cards.pop(index)
	def remove_card(self, card: Card):
		self.cards.remove(card)
	def pick_rand(self):
		card = self.rand_card()
		self.remove_card(card)
		return card

def create_deck() -> Deck:
	deck = []
	for suit in ["♠", "♥", "♦", "♣"]:
		for i in range(1,14):
			deck.append(Card(i, suit))
	return Deck(deck)
