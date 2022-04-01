import random
start = input('Please define the value of starting point:')
start = int(start)
end = input('Please define the value of ending point:')
end = int(end)
r = random.randint(start, end)
count = 0 # counting times of guess
while True:
	count += 1  # count = count + 1
	num = input('Please take a guess of a random number: ')
	num = int(num)
	if num == r:
		print('Bingo!')
		print('This is your ', count, 'attempt(s).')
		break
	elif num > r:
		print('Your answer is greater than the answer.')
	elif num < r:
		print('Your answer is lower than the answer.')
	print('This is your ', count, 'attempt(s).')