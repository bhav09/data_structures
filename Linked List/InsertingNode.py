# INSERTING NODE INTO A LINKED LIST

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
	
	def PrintAll(self):
		temp=self.head
		if temp == None:
			print('Inserting into linked list')
		while temp:
			print(temp.data,'->',end='')
			temp=temp.next
	
	# Insert beg
	def Push(self,new_data):
		new_node=Node(new_data)
		new_node.next=self.head
		self.head=new_node
	
	# Insert end
	def Append(self,new_data):
		new_node=Node(new_data)
		if self.head is None:
			print('List was empty')
			self.head=new_node
		else:
			temp=self.head
			while temp.next is not None:
				temp=temp.next
			temp.next=new_node
			
	# Insert after
	def InsertAfter(self,value,new_data): 
		new_node=Node(new_data)
		temp=self.head
		while temp is not None:
			if temp.data==value:
				ref=temp.next
				temp.next=new_node
				new_node.next=ref
				break
			else:
				temp=temp.next
	
	# Insert Before
	def InsertBefore(self,value,new_data):
		temp=self.head
		prev=temp
		new_node=Node(new_data)
		if self.head is not None:
			if value==self.head.data:
				new_node.next=self.head
				self.head=new_node
				return
		else:
			print('List is empty')
			return
		
		while temp is not None:
			if temp.data==value:
				prev.next=new_node
				new_node.next=temp
				break
			prev=temp
			temp=temp.next
	
#driver code ;)
l=LinkedList()
l.Append(1)
l.Append(2)
l.Append(3)
l.InsertAfter(2,4)
l.InsertBefore(4,5)
l.InsertBefore(3,6)
l.PrintAll()
