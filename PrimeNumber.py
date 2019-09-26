num = 2
primeNumbers = []
while num < 10000 :
	i = 2
	flag = True
	while i < num :
		if num % i == 0 :
			flag = False
			break
		i = i + 1
	if flag == True : primeNumbers.append(num)
	num = num + 1
while 1 :
	flag = True
	for primeNumber in primeNumbers :
		if num % primeNumber == 0 : flag = False
	if flag == True :
		primeNumbers.append(num)
		print(num)
	num = num + 1
