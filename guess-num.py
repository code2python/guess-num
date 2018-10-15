import random 

r = random.randint (1, 100)
while True:
	num = input('Please guess a number: ')
	num = int (num)
	if num == r:
		print('Bingo!!')
		break
	elif num > r:
		print ('the number that you have enter is bigger than me')

	elif num < r:
		print ('the number that you have enter is smaller than me')