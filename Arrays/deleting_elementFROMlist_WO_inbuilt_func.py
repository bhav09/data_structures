def delete(a,idx):
	for i in range(idx,len(a)-1,1):
		a[i]=a[i+1]
	a=a[:-1]
	return a

a=[1,2,3,4]
idx=int(input('Enter index whose value you want to delete?'))
my_list=delete(a,idx)
print(my_list)