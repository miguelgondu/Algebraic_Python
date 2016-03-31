class Pregroup:
	'''
	A Pregroup is just a set with an operation. The operation doesn't
	need to be associative, modulative or invertive. Once those three
	conditions are satisfied, a Pregroup can be also called as a group.
	The set S = _set that the Pregroup object takes is a normal python set,
	and the operation is a set of tuples of the form ((a,b), c) which
	implies a*b=c, the operation must have for every pair of elements of S
	the value of their operation. Otherwise an error is raised.


	This class commes with functions that determine whether or not the 
	operation is associative, modulative or invertive. (These last two
	are not yet included, and they are a TO-DO)
	'''

	def __init__(self, _set, _operation):
		self.Pregroup_set = _set
		self.Pregroup_operation = _operation

		# Checking if arguments are indeed a sets
		if type(self.Pregroup_set) != type({0,1}) or type(self.Pregroup_operation) != type({0,1}):
			raise ValueError('Both arguments should be sets.')


		# Checking if the operation is correctly defined

		for _tuple in self.Pregroup_operation:
			if _tuple[0][0] not in self.Pregroup_set:
				raise ValueError('Elements in operation should belong to the set.')
			if _tuple[0][1] not in self.Pregroup_set:
				raise ValueError('Elements in operation should belong to the set.')
			if _tuple[1] not in self.Pregroup_set:
				raise ValueError('Elements in operation should belong to the set.')

		# Checking if there's a value for every possible pair

		Counter_of_pairs_with_operation_value = 0
		for element1 in self.Pregroup_set:
			for element2 in self.Pregroup_set:
				for _tuple in self.Pregroup_operation:
					if _tuple[0][0] == element1 and _tuple[0][1] == element2:
						Counter_of_pairs_with_operation_value += 1

		if Counter_of_pairs_with_operation_value < len(self.Pregroup_set) ** 2:
			raise ValueError('There is a pair of elements without value in operation.')

	def printPregroupTable(self, string='*'):
		'''
		Prints the pregroup table.
		- string: is a string which represents the operation. Default is an asterisk
		TO-DO: Fix spaces depending on how big the elements in the set are.
		'''
		print(str(string) +' | ', end='')
		for element in self.Pregroup_set:
				print(str(element) + ' | ', end='')
		print()
		for element1 in self.Pregroup_set:
			print(str(element1), end=' | ')
			for element2 in self.Pregroup_set:
				for _tuple in self.Pregroup_operation:
					if _tuple[0] == (element1, element2):
						print(_tuple[1], end=' | ')
			print()

	def operate(self, a, b):
		if a in self.Pregroup_set and b in self.Pregroup_set:
			pass
		else:
			raise ValueError('Objects must belong to the pregroup.')
				

		for _tuple in self.Pregroup_operation:
			if _tuple[0][0] == a and _tuple[0][1] == b:
				return _tuple[1]

	def isPregroupAssociative(self, Printing_flag):
		Counter_of_associativeness = 0
		for x in self.Pregroup_set:
			for y in self.Pregroup_set:
				for z in self.Pregroup_set:
					if self.operate(self.operate(x,y), z) == self.operate(x,self.operate(y,z)):
						Counter_of_associativeness += 1
					elif Printing_flag == True:
						print('('+str(x)+'*'+str(y)+')'+'*'+str(z)+'!='+str(x)+'*'+'('+str(y)+'*'+str(z)+')')

		if Counter_of_associativeness < len(self.Pregroup_set) ** 3:
			return False
		elif Counter_of_associativeness == len(self.Pregroup_set) ** 3:
			return True

class Group:
	'''
	A group object takes a set of elements and an operation. The set S =_set
	is a normal python set, and the operation is a set of tuples in which
	the first element is a tuple of elements of S in and the second is an
	element from S, that is, a tuple ((a,b), c) implies that a*b = c in
	the group.

	TO-DO: 
	- To check whether or not is the group well-defined, assert the creation
	  of a pregroup that must be associative, modulative and invertive.
	- how can I check that _operation is defined with elements in S?
	- Create a function that generates (Zn, +) and other usual groups
	  -- Create an arithmetic on Zn which recognizes equivalence classes
	- Is it possible to work with infinite groups?
	'''
	
	def __init__(self, _set, _operation):
		self.Group_set = _set
		self.Group_operation = _operation

		G = Pregroup(_set, _operation)

	def getGroupSet(self):
		return self.Group_set

	def getGroupOrder(self):
		return len(self.Group_set)

	def operate(self, a, b):
		if a in self.Group_set and b in self.Group_set:
			pass
		else:
			raise ValueError('Objects must belong to the group.')
				

		for _tuple in self.Group_operation:
			if _tuple[0][0] == a and _tuple[0][1] == b:
				return _tuple[1]

	def printGroupTable(self):
		print('* | ', end='')
		for element in self.Group_set:
				print(str(element) + ' | ', end='')
		print()
		for element1 in self.Group_set:
			print(str(element1), end=' | ')
			for element2 in self.Group_set:
				for _tuple in self.Group_operation:
					if _tuple[0] == (element1, element2):
						print(_tuple[1], end=' | ')
			print()

	def isGroupAbelian(self):
		Counter_of_non_abelian_pairs = 0
		for _tuple1 in self.Group_operation:
			for _tuple2 in self.Group_operation:
				if _tuple1[0][0] == _tuple2[0][1] and _tuple1[0][1] == _tuple2[0][0]:
					if _tuple1[1] != _tuple2[1]:
						Counter_of_non_abelian_pairs += 1

		if Counter_of_non_abelian_pairs > 0:
			return False
		elif Counter_of_non_abelian_pairs == 0:
			return True


						
