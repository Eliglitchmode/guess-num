import random
r = random.randint(1, 100)

while True:
	num = input('Please take a guess of a random number: ')
	num = int(num)
	if num == r:
		print('Bingo!')
		break
	elif num > r:
		print('Your answer is greater than the answer.')
	elif num < r:
		print('Your answer is lower than the answer.')