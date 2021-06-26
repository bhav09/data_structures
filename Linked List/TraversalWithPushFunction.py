# Traversal with user input

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
			print(temp.data,'->' ,end='')
			temp=temp.next

obj=LinkedList()
obj.Push(4)
obj.Push(2)
obj.Push(3)
obj.PrintAll()