class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def AddStart(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

	def AddEnd(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node
		new_node.prev = last
		return

	def DeleteAtStart(self):
		if self.head is None:
			print("Tidak ada elemen untuk dihapus")
			return
		if self.head.next is None:
			self.head = None
			return
		self.head = self.head.next
		self.head.prev = None

	def DeleteAtEnd(self):
		if self.head is None:
			print("Tidak ada elemen untuk dihapus")
			return
		if self.head.next is None:
			self.head = None
			return
		n = self.head
		while n.next is not None:
			n = n.next
		n.prev.next = None


	def Search(self,data):
					temp = self.head
					while temp:
							if temp.data==data:
									break
							temp = temp.next
					if temp==None:
							print("The given data doesnt exist:")
							return False
					return True

	def view(self):
		print ("list data doubly linked list:")
		current_node = self.head
		while current_node is not None:
			print (current_node.data)
			current_node = current_node.next