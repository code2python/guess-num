import random 

r = random.randint (1, 100)
count = 0
while True:
	num = input('Please guess a number: ')
	num = int (num)
	count += 1  # count = count + 1  
	if num == r:
		print('Bingo!!')
		print ('this is your', count, 'guess')
		break
	elif num > r:
		print ('the number that you have enter is bigger than me')

	elif num < r:
		print ('the number that you have enter is smaller than me')

	print ('this is your', count, 'guess')