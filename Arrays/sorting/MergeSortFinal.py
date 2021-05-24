def Merge(a,l,r):
	m=len(l)
	n=len(r)
	i,j,k=0,0,0
	while i<m and j<n:
		if l[i]<r[j]:
			a[k]=l[i]
			i+=1
			k+=1
		else:
			a[k]=r[j]
			j+=1
			k+=1
	while i<m:
		a[k]=l[i]
		i+=1
		k+=1
	while j<n:
		a[k]=r[j]
		j+=1
		k+=1
	return a
			

def MergeSort(a):
	if len(a)>1:
		m=len(a)//2
		l=a[:m]
		r=a[m:]
		MergeSort(l)
		MergeSort(r)
		return Merge(a,l,r)
	
a=[3,1,6,4,7,2,9]
arr=MergeSort(a)
print(arr)