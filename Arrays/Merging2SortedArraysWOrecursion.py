#merging 2 sorted arrays using function
def merge(a,b,m,n):
	while m<len(a) and n<len(b):
		if a[m]<b[n]:
			merged.append(a[m])
			m+=1
		else:
			merged.append(b[n])
			n+=1
	while m<len(a):
		merged.append(a[m])
		m+=1
	while n<len(b):
		merged.append(b[n])
		b+=1
	return merged
a=[1,3,4,6,8]
b=[2,5,6]
merged=[]
print(merge(a,b,0,0))