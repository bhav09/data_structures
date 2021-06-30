# Nth node from last

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
			print(temp.data,'->',end='')
			temp=temp.next
	
	def Append(self,new_data):
		new_node=Node(new_data)
		if self.head==None:
			self.head=new_node
		else:
			temp=self.head
			while temp.next is not None:
				temp=temp.next
			temp.next=new_node
	
	def Push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node
	
	def NfromLast(self,n):
		count=0
		print()
		temp=self.head
		while temp:
			temp=temp.next
			count+=1
		#print(count)
		if n>count:
			print('Invalid')
		else:
			c=1
			temp=self.head
			while temp:
				temp=temp.next
				c+=1
				if c==count+1-n:
					print('Nth node from Last is:',temp.data)
					break

l=LinkedList()
l.Append(1)
l.Append(2)
l.Push(3)
l.Append(4)
l.Push(5)
l.PrintAll()
l.NfromLast(4)