#arraying containing zeros come the leftmost side of the array without distrubing the order of non zero elements
def ShiftZero2Right(arr):
	count=0
	for i in range(len(arr)):
		if arr[i]!=0:
			arr[count],arr[i]=arr[i],arr[count]
			count+=1
	return arr

a=[10,5,0,0,8,0,9,0]
new_arr=ShiftZero2Right(a)
print(new_arr)