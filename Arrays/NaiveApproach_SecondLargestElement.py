#returning the index of the second largest element
def SecondLargest(arr):
	max_ele=arr[0]
	for i in range(len(arr)):
		if arr[i]>max_ele:
			max_ele=arr[i]
	sec=-1
	for i in range(len(arr)):
		if arr[i]!=max_ele:
			if arr[i]>sec:
				sec=arr[i]
	if sec==-1:
		print('No second largest element')
	else:
		 print('Second Largest Element is:',sec)
	 
a=[4,2,1,7,9,12]
SecondLargest(a)