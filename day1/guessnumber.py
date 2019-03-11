number=-1
guess=10
while(number!=10):
	number = input('Please type in a number here: ')
	if int(number)<10:
		print('too small!')
	elif int(number)>10:
		print('too large')
	elif int(number==10):
		print('Bingo!')
		break