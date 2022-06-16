# import required module
import random
import os


def get_chances(difficulties):
	# ask the user for difficulty level
	difficulty = input("Type " + (" or ".join([f"'{dif}' to get {difficulties[dif]} chances" for dif in difficulties])) + ": ").lower()
	# if the typed difficulty level is not in the difficulties dict, return the maximum chances
	if difficulty not in difficulties:
		return max(difficulties.values())
	# else return the number of chances  as per the given difficulties dict
	return difficulties[difficulty]


def check_guess(guess, number):
	# if the guess is equal to the random number picked, then display 'they won' and break the loop
	if guess == number:
		print(f"Wow! You found the number! It was {number}. You win...\n")
	# else if their guess is less than the number, then display 'too low'
	elif guess < number:
		print("Too low...\n")
	# else if their guess is greater than the number, then display 'too high'
	else:
		print("Too high...\n")


def main():
	# clears the screen
	os.system("clear")
	
	print("Welcome to our Number Guessing Game!...\n")
	
	# pick a random number between 1 and 100
	number = random.randint(1, 100)
	print("I'm thinking a number between 1 and 100.")

	# give number of chances based on their chosen difficulty level: 10 for easy, 7 for normal and 5 for hard.
	chances = get_chances({"easy": 10, "normal": 7, "hard": 5})
	
	print()
	# loop until they run out of chances
	while chances > 0:
		# display the chances left
		print(f"You have {chances} chances left to guess the number!")
		
		# ask the user for a guess
		guess = int(input("Type your guess: "))
		# check user's guess with the random number picked and display too high, too low, or you won
		check_guess(guess, number)
		# if they guessed the number correctly, then break the loop
		if guess == number:
			break
		# decrement the chances by 1
		chances -= 1
	
	# if ran out of chances without guessing the right number, then display 'they lose'
	if not chances and guess != number:
		print(f"Sorry! You are out of chances and you haven't found the number! It was {number}. You lose...\n")

	# ask the user whether they would like to play again
	if input("Would you like to play again? Type 'yes' or 'no': ").lower() == "yes":
		main()


if __name__ == "__main__":
	main()


