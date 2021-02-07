#finding kth smallest element
#with inbuilt function

def KthMinimum(k,my_list):
	new_list=sorted(my_list)
	return new_list[k-1]

n=int(input('Enter number of elements:'))
l=[]
for i in range(n):
	l.append(int(input('Enter Element:')))
print(l)	
k=int(input('Enter the value of K:'))
val=KthMinimum(k,l)
print(val)