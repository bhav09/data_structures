def SelectionSort(my_list):
	for i in range(len(my_list)):
		minn=i
		for j in range(i+1,len(my_list)):
			if a[minn]>a[j]:
				idx=j
				minn=j
		a[minn],a[i]=a[i],a[minn]
	return my_list

a=[5,3,8,6,7,2]
new_list=SelectionSort(a)
print(new_list)