import random 
start = input('please determine the digit range start value')
end = input('please determine the digit range ending value')
start = int(start)
end = int(end)

r = random.randint(start , end)
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