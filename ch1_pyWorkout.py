#pyWorkout_ch1.py

import random

number = random.randint(10, 30)
print(number)
"""
name = input('Enter your name: ')
print(f'Hello, {name}!')
"""
def guessing_game():

	rand_int = random.randint(0, 100)
	

	while True:
		guess_int = int(input('Enter your guess between 0-100: '))
		
		if guess_int == rand_int:
			print('You win')
			break

		if guess_int < rand_int:
			print('Too low')
		if guess_int > rand_int:
			print('Too high')


#guessing_game()


print(40*.1, 40*.7, 40*.2)