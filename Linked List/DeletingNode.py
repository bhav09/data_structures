# Deleting Node in Linked List

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
	
	def Append(self,new_data):
		temp=self.head
		new_node=Node(new_data)
		if self.head==None:
			self.head=new_node
		else:
			while temp.next is not None:
				temp=temp.next
			temp.next=new_node
	
	def DeleteBeg(self):
		temp=self.head
		ref=temp.next
		self.head=ref
	
	def DeleteEnd(self):
		temp=self.head
		while temp.next is not None:
			prev=temp
			temp=temp.next
		prev.next=None	

	def DeleteBetween(self,value):
		temp=self.head
		prev=temp
		while temp:
			if temp.data==value:
				prev.next=temp.next
				temp.next=None
			prev=temp
			temp=temp.next
		
	def PrintAll(self):
		temp=self.head
		while temp:
			print(temp.data,'-> ',end='')
			temp=temp.next

l=LinkedList()
for i in range(1,8):
	l.Append(i)
llist=l
l.PrintAll()
print('\nAfter deleting the first node')
l.DeleteBeg()
l.PrintAll()
print('\nAfter deleting the last node')
l.DeleteEnd()
l.PrintAll()
print('\nAfter deleting the node in between')
l.DeleteBetween(3)
l.PrintAll()