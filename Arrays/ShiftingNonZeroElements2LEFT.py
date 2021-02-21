#arraying containing zeros come the leftmost side of the array without distrubing the order of non zero elements

def ShiftZero2Right(arr):
	if 0 not in arr:
		return arr
	else:
		for i in range(len(arr)-1):
			if arr[i]==0:
				for j in range(i,len(arr)-1):
					if arr[j]!=0:
						arr[i],arr[j]=arr[j],arr[i]
						break
		return arr

a=[10,5,0,0,8,0,9,0]
new_arr=ShiftZero2Right(a)
print(new_arr)