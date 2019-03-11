import random

number=random.randint(1,20)
print(number)
guess=0

while(guess!=number):
	inputvalue = input('Please type in a number here: ')
	guess=int(inputvalue)
	if guess<number:
		print('too small!')
	elif guess>number:
		print('too large!')
if int(guess==number):
	print('Bingo!')

