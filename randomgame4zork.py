import random
num = random.randint(1, 50)
while True:
	print('Guess a number between 1 and 100')
	guess = input()
	i = int(guess)
	if i == num:
		print('you guessed right')
	elif i < num:
		print('try higher')
	elif i > num:
		print('try lower m8')