def qsort(a,l,h):
	if l<h:
		_,sep=HoarePartition(a,l,h)
		qsort(a,l,sep)
		qsort(a,sep+1,h)
		return a

def HoarePartition(a,l,h):
	pivot=a[l]
	i,j=l-1,h+1
	i+=1
	while True:
		while a[i]<pivot:
			i+=1
		j-=1
		while a[j]>pivot:
			j-=1
		if i>=j:
			return a,j
		a[i],a[j]=a[j],a[i]
	
a=[5,3,8,4,2,7,1,10]
#new_arr,sep=HoarePartition(a,0,len(a)-1)
#print('Separation begins from index:',sep)
#print('Partitioned Array:',new_arr)
qsort(a,0,len(a)-1)	