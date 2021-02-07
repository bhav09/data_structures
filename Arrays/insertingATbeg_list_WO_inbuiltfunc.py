#inserting element at the first position in list
def insert_beg(l,val):
	l+=[-1]
	for i in range(len(l)-1,0,-1):
		l[i]=l[i-1]
	l[0]=val
	return l


a=[1,2,3,4]
val=int(input('Enter value to insert at the beg:'))
new_list=insert_beg(a,val)
print(new_list)