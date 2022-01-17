def most_frequent():
	a = input("Please enter a string\n")
	count = {}
	for i in a:
		if i in count:
			count[i] +=1
		else:
			count[i] = 1
	print("i = ",count['i'])
	print("s = ",count['s'])
	print("p = ",count['p'])
	print("m = ",count['M'])
most_frequent()