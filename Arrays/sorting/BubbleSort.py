#finding kth minimum and kth maximum without using inbuilt functions

def BubbleSort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1):
			if a[j]>a[j+1]:
				a[j],a[j+1]=a[j+1],a[j]
	return arr

a=[3,9,7,5,2,-3,4]
a=BubbleSort(a)
print(a)