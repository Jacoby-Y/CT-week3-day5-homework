import os
from cli import run 

def main():
	wins = 0
	losses = 0
	while True:
		print("===============================")
		print(f"   ————— Win/Loss: {wins}/{losses} —————")
		print("===============================")
		if run():
			wins += 1
		else:
			losses += 1
		inp = input("\nPlay again? Yes / No\n> ").lower()[0]
		if inp == "n":
			break
		os.system('cls' if os.name == 'nt' else 'clear')
	print(f"You won {int(wins/(wins+losses)*100)}% of the time")

if __name__ == "__main__":
	main()
