# Recursive Traversal

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LList:
	def __init__(self):
		self.head=None
	
	def PrintList(self,node):
		self.node=node
		if self.node.data==None:
			return
		if self.node.next==None and self.node.data!=None:
			print(self.node.data)
			return
		else:
			print(self.node.data)
			self.node=self.node.next
			self.PrintList(self.node)

obj=LList()

obj.head=Node(1)
val2=Node(2)
val3=Node(3)

obj.head.next=val2
val2.next=val3

obj.PrintList(obj.head)