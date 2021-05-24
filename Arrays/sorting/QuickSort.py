#quicksort
def qsort(a,l,h):
	if l<h:
		_,pivot=LomutoPartition(a,l,h)
		qsort(a,l,pivot-1)
		qsort(a,pivot+1,h)
		return a
		
def LomutoPartition(a,l,h):
	i,j=-1,-1
	pivot=a[h]
	while i<len(a) and j<len(a):
		if a[i]<=pivot:
			a[i],a[j]=a[j],a[i]
			j+=1
		i+=1
	return a,j-1

a=[8,4,7,9,3,10,5]
#LomutoPartition(a,0,len(a)-1)
qsort(a,0,len(a)-1)