def partition(a,idx):
	k,i=0,0
	if idx!=len(a)-1:
		a[idx],a[len(a)-1]=a[len(a)-1],a[idx]
		idx=len(a)-1
	while i<len(a) and k<len(a):
		if a[i]<=a[idx]:
			a[k],a[i]=a[i],a[k]
			k+=1
		i+=1
	return a

a=[4,1,7,3,8,6]
idx=a.index(7)
#partition(a,idx)
print(partition(a,idx))