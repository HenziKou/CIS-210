# DICE 2 EXAMPLE

def roll_dice():
	'''
	'''

	roll1 = random.randint(1, 6)
	roll2 = random.randint(1, 6)

	print(roll1, ",", roll2)
	return None


for i in range(30):
	roll_dice()