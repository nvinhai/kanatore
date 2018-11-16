import csv, random

#Constants
NUM_ROUNDS = 10
NUM_CHOICES = 5

def get_option():
	print("\nSelect what you would like to practice: ")
	print("1. Hiragana / ひらがな")
	print("2. Katakana / カタカナ")
	print("3. Both")
	print("\nEnter anything else to exit.")

	return input("Your option: ")

def get_kana_from_csv():
	hiragana = []
	katakana = []

	#Read Hiragana
	with open('hiragana.csv', 'r') as hiragana_file:
		hreader = csv.reader(hiragana_file)

		for line in hreader:
			hiragana.append(line)

	#Read Katakana
	with open('katakana.csv', 'r') as katakana_file:
		kreader = csv.reader(katakana_file)

		for line in kreader:
			hiragana.append(line)
	
	return hiragana, katakana
def random_kana(library):
	return library[random.randint(0, len(library)-1)]

def print_round(round,score):
	print(19*"-")
	print("Round {:2d} | Score: {}".format(round+1,score))
	print(19*"-")

def get_multiple_choice(question, library):
	#Builds a list of choices which includes the question.
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	choices = []

	#Populate choices with random numbers
	for x in range(NUM_CHOICES-1):
		toAdd = random_kana(library)
		while toAdd in choices or toAdd == question[1]:
			toAdd = random_kana(library)
		choices.append(toAdd[0])

	#Insert the correct choice into a random index of choices
	correct_index = random.randint(0,NUM_CHOICES)
	choices.insert(correct_index,question[0])

	for i in range(len(choices)):
		print("{}) {}".format(alphabet[i],choices[i]))

	return alphabet[correct_index]

def main_game(option):
	print()
	score = 0
	library = []
	hiragana, katakana = get_kana_from_csv()

	if option == "1":
		library = hiragana
	elif option == "2":
		library = katakana
	elif option == "3":
		library = hiragana + katakana
	else:
		return "n"
	
	for round in range(NUM_ROUNDS):
		print()

		#Pull a random kana from the library.
		question = random_kana(library)
		
		print_round(round,score)
		
		print("What is the correct reading of: {}?".format(question[1]))
		correct_answer = get_multiple_choice(question,library)

		user_answer = input("\nEnter your answer: ")

		if user_answer == correct_answer:
			print("Correct! Good job!")
			score+=1
		else:
			print("Incorrect! The answer was {}, '{}'.".format(correct_answer, question[0]))
		
	print("\nTotal Score: {}".format(score))
	return input("Would you like to play again? (y/n): ")