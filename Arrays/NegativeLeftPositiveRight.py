#Move all negative numbers to beginning and positive to end

def CustomShuffle(arr):
	neg=[]
	for i in arr:
		#print(i)
		if (i<0):
			val=i
			neg.append(val)
	#print(neg)
	for value in arr:
		if value<0:
			arr.pop(arr.index(value))
	neg=neg+arr
	return neg

arr=[]
for i in range(5):
	arr.append(int(input('Enter Element:')))
new_arr=CustomShuffle(arr)

print('After Custom Shuffling:',new_arr)
