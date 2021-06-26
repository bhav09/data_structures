# Linear Search iterative 

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
	
	def Search(self,target):
		temp=self.head
		flag=0
		while temp:
			if temp.data==target:
				flag=1
				break
			temp=temp.next
		if flag==1:
			print('Element Found')
		else:
			print('Not found')

obj=LinkedList()
obj.Push(1)
obj.Push(2)
obj.Push(3)
obj.Push(4)
obj.Search(3)