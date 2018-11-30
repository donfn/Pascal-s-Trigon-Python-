def PascalTrigonRow(n):
	trigon=[]
	for i in range(n):
		trigon.append(i)
		trigon[i] = []
		for a in range(1,i+2):
			if a == 1 or a == i+1:
				trigon[i].append(1)
			else:
				trigon[i].append(trigon[i-1][a-2] + trigon[i-1][a-1])
	return trigon[n-1]

print(PascalTrigonRow(int(input('Which row do you want? '))))
