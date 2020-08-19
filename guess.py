import random 

r = random.randint(1 , 100)
while True:
	count += 1 
	num = inpit('please guess the random number:')
	num = int(num)
	if num == r:
		print('your answer is right')
		print('these are your guess number', count , 'times')
		break
    elif num > r:
    	print('your answer is more than original')
    elif num < r:
    	print('your answer is less than original')
    print('these are your guess number', count , 'times')