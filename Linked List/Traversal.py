# Linked List Traversal

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
		
	def PrintList(self):
		temp=self.head
		while temp:
			print(temp.data)
			temp=temp.next

#object initialisation
obj=LinkedList()

#putting in values to the nodes
obj.head=Node(1)
val2=Node(2)
val3=Node(3)

#setting references
obj.head.next=val2
val2.next=val3
	
#printing linkedin list
obj.PrintList()