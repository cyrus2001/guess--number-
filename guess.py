import random 

r = random.randint(1 , 100)
while True:
	num = inpit('please guess the random number:')
	num = int(num)
	if num == r:
		print('your answer is right')
		break
    elif num > u:
    	print('your answer is more than original')
    elif num < r:
    	print('your answer is less than original')