#merging sorted arrays using recursion
def merge(a,b,ia,ib):
	print(ia,ib)
	if ia<len(a) and ib<len(b):
		if a[ia]>b[ib]:
			merged.append(b[ib])
			#print(merged)
			return merge(a,b,ia,ib+1)
		elif a[ia]<b[ib]:
			merged.append(a[ia])
			#print(merged)
			return merge(a,b,ia+1,ib)
	elif ib==len(b)-1:
		merged.append(b[ib])
	elif ia==len(a)-1:
		merged.append(a[ia])
				
a=[1,4,6,9]
b=[2,3,5,7]
merged=[]
merge(a,b,0,0)
print(merged)