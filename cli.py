''' ♠ ♥ ♦ ♣ ♤ ♡ ♢ ♧
Dealer: ??, Ace♠

You: Jack♥, 5♥


Hit or Stay?
> 
'''

from deck import create_deck, Card

def get_hand_value(hand: list[Card]):
	return sum([card.value for card in hand])

def has_card_num(hand: list[Card], num):
	for card in hand:
		if card.value == num:
			return True
	return False


def get_hand_value(hand: list[Card]) -> int:
	total = 0
	values = [card.value for card in hand]
	for i, val in enumerate(sorted(values, reverse=True)):
		if val == 1:
			if total + 11 > 21:
				pass
			elif total + 11 == 21 and i == len(values)-1:
				return True
			elif total + 11 < 21:
				total += 10
		total += val
	return total

def has_21(hand: list[Card]):
	return get_hand_value(hand) == 21

def pr_hand(hand: list[Card], show_all=False):
	if show_all:
		for card in hand:
			card.hidden = False
	return ", ".join([i.__str__() for i in hand])

def run() -> bool:
	deck = create_deck()

	dealer_hand: list[Card] = [deck.pick_rand(), deck.pick_rand()]
	user_hand: list[Card] = [deck.pick_rand(), deck.pick_rand()]
	dealer_hand[0].hidden = True

	if has_21(dealer_hand):
		dealer_hand[0].hidden = False
		print(f"Dealer: {pr_hand(dealer_hand)}\n")
		print("Welp, the deal wins!")
		return False

	stay = False

	while True:
		print(f"Dealer: {pr_hand(dealer_hand)}\n")
		
		if has_21(user_hand):
			print(f"You: {pr_hand(user_hand)} ({get_hand_value(user_hand)})\n")
			print("Hey, you win!")
			return True
		
		if get_hand_value(user_hand) > 21:
			print(f"You: {pr_hand(user_hand)} ({get_hand_value(user_hand)})\n")
			print("Yeah... Maybe you shouldn't have hit.")
			return False

		print(f"You: {pr_hand(user_hand)} ({get_hand_value(user_hand)})\n")

		while True:
			inp = input("Hit or Stay?\n> ").lower()[0]
			if inp == "h":
				print("————————————————————————")
				user_hand.append(deck.pick_rand())
				break
			elif inp == "s":
				stay = True
				break
			print("What?")
		if stay:
			break
		
	d_value = get_hand_value(dealer_hand)
	u_value = get_hand_value(user_hand)
	print("————————————————————————")
	if d_value >= 17:
		if u_value <= d_value:
			print(f"Dealer: {pr_hand(dealer_hand, True)} ({get_hand_value(dealer_hand)})\n")
			print(f"You: {pr_hand(user_hand)} ({get_hand_value(user_hand)})\n")
			print("———— Ahhh, the house beat you!!")
			return False
		elif u_value <= 21:
			print(f"Dealer: {pr_hand(dealer_hand, True)} ({get_hand_value(dealer_hand)})\n")
			print(f"You: {pr_hand(user_hand)} ({get_hand_value(user_hand)})\n")
			print("———— Hey, you won?? Nice.")
			return True
	else:
		while True:
			dealer_hand.append(deck.pick_rand())
			d_value = get_hand_value(dealer_hand)
			u_value = get_hand_value(user_hand)
			if d_value > 21:
				print(f"Dealer: {pr_hand(dealer_hand, True)} ({get_hand_value(dealer_hand)})\n")
				print(f"You: {pr_hand(user_hand)} ({get_hand_value(user_hand)})\n")
				print("———— Huh, you won... Ok.")
				return True
			elif d_value >= u_value:
				print(f"Dealer: {pr_hand(dealer_hand, True)} ({get_hand_value(dealer_hand)})\n")
				print(f"You: {pr_hand(user_hand)} ({get_hand_value(user_hand)})\n")
				print("———— You lost?? Ah, sooo sad... (:")
				return False