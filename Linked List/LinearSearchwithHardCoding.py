# Linear Search

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		
class LinkedList:
	def __init__(self):
		self.head=None
		
	def LinearSearch(self,x):
		temp=self.head
		count=0
		flag=0
		while temp:
			if temp.data==x:
				flag=1
				break
			temp=temp.next
			count+=1
		if flag==1:
			print('Element Found at Node ',count)
		else:
			print('Not Found')
		
obj=LinkedList()
obj.head=Node(1)
val2=Node(2)
val3=Node(3)

obj.head.next=val2
val2.next=val3

obj.LinearSearch(2)
