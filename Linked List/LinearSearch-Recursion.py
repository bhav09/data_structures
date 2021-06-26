# Linear Search Recursion

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
	
	def Push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node
	
	def PrintAll(self):
		temp=self.head
		while temp:
			print(temp.data)
			temp=temp.next
	
	def Search(self,node,target):
		if not obj:
			return False

		n=node
		val=target
		if n.data==val:
			return True
		return self.Search(n.next,val)

l=LinkedList()
l.Push(1)
l.Push(2)
l.Push(3)
l.Search(l.head,2)
