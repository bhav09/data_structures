#rotating one element in the clockwise direction

def RotatebyOne(arr):
	l=len(arr)
	temp=arr[l-1]
	for i in range(0,len(arr)):
		arr[l-i-1]=arr[l-i-2]
	arr[0]=temp
	return arr

arr=[9,4,5,3,7,2]
print('Original Array:',arr)
new_arr=RotatebyOne(arr)
print('New Array:',new_arr)