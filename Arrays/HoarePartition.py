def partition(a,l,h):
	#pivot's always the first element
	pivot=a[l]
	i,j=l-1,h+1
	while True:
		i+=1
		while a[i]<pivot:
			i+=1
		j-=1
		while a[j]>pivot:
			j-=1
		if i>=j:
			return a,j
		a[i],a[j]=a[j],a[i]

a=[5,3,8,4,2,7,1,10]
new_arr,sep=partition(a,0,len(a)-1)
print('Separation begins from index:',sep)
print('Partitioned Array:',new_arr)	