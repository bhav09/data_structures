def insert(a,idx,val):
	a+=['']
	for i in range(len(a)-1,idx,-1):
		a[i]=a[i-1]
	a[idx]=val
	return a

a=[1,2,4,5]
idx=int(input('Enter index:'))
val=int(input('Enter Value:'))
new_list=insert(a,2,3)
print(new_list)