import functions, json

print()
print(43*"-")
print("Welcome to KanaTore! | かなトレへようくそ！")
print(43*"-")

start = (input("Would you like to start a new game? (y/n): ")[0:1]).lower()

while start == "y":
	option = functions.get_option()

	start = functions.main_game(option)

