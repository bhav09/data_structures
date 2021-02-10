#insertion sort
def InsertionSort(arr):
	for i in range(1,len(arr)):
		 var=arr[i]
		 j=i-1
		 while j>=0 and var<arr[j]:
			 arr[j+1]=arr[j]
			 j-=1
		 arr[j+1]=var
	return arr


arr=[5,3,7,4,9,2]
new_arr=InsertionSort(arr)
print('Sorted Array:',new_arr)