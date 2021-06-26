class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
		
	def PrintAll(self):
		temp=self.head
		while temp:
			print(temp.data,'->',end=' ')
			temp=temp.next
	
	def append(self,new_data):
		new_node=Node(new_data)
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while temp.next is not None:
				temp=temp.next
			temp.next=new_node
	
	def reverse(self):
		temp=self.head
		prev=None
		while temp is not None:
			ref=temp.next
			temp.next=prev
			prev=temp
			temp=ref
		self.head=prev
			
			
l=LinkedList()
for i in range(5):
	l.append(i)
l.PrintAll()
l.reverse()
print()
l.PrintAll()