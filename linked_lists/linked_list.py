# creating a node class
class node:
	def __init__(self,dataval=None):
		self.dataval = dataval
		self.nextval = None


#creating an address class for keeping track of the position in the linked list
class address:
	def __init__(self):
		p = None
		c = None

#linked list class and different custom methods
class linkedList:
	def __init__(self):
		self.headval = None
	def print_list(self):
		v = self.headval
		while v != None:
			print(v.dataval)
			v = v.nextval
	def insert_top(self,node_val):
		n = node(node_val)
		n.nextval = self.headval
		self.headval = n
	def insert_last(self,last_value):
		n = node(last_value)
		v = self.headval
		while True:
			if v.nextval == None:
				v.nextval = n
				break
			else:
				v = v.nextval
	def insert_between(self,new_node,existing_node):
		n = node(new_node)
		n.nextval = existing_node.nextval
		existing_node.nextval = n
	def delete_node(self,reference):
		if self.headval.dataval == reference:
			self.headval = self.headval.nextval
			return print('Done!')
		m = address()
		m.p = self.headval
		m.c = self.headval.nextval
		if m.c.dataval == reference:
			m.p.nextval = m.c.nextval
			m.c = None
			return print('Done')
		while m.c.nextval != None:
			m.p = m.p.nextval
			m.c = m.c.nextval
			if m.c.dataval == reference:
				m.p.nextval = m.c.nextval
				m.c = None
				return print('Done')
		print('Not found')

        