'''
Group_theory.py, by MGD.

In this file, the main objects of group theory are defined:
- A pregroup is a set with an operation, said operation may not even be
  associative, nor modulative or inverible. But it does have to be
  defined on the set that is passed. 
- A group is a set with an operation that is indeed associative,
  modulative and invertible.
For more information, check the documentation of each object.

TO-DO:
 - Create a function that translates a csv file into an operation.
'''

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

		# TO-DO: _operation might not be a function. Check that.

		Counter_of_double_values = 0
		for _tuple1 in self.Pregroup_operation:
			for _tuple2 in self.Pregroup_operation:
				if _tuple1[0] == _tuple2[0]:
					if _tuple1[1] != _tuple2[1]:
						Counter_of_double_values += 1

		if Counter_of_double_values > 0:
			raise ValueError('Operation is not a function.')

	def getPregroupSet(self):
		'''
		Returns the underlying set of the Pregroup.
		'''
		return self.Pregroup_set

	def getPregroupOrder(self):
		'''
		Returns the amount of elements in the underlying set of 
		the pregroup 
		'''
		return len(self.Pregroup_set)

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
		'''
		Returns the result of operating element a and b in that order.
		The elements a and b must belong to the Pregroup set.
		'''
		if a in self.Pregroup_set and b in self.Pregroup_set:
			pass
		else:
			raise ValueError('Objects must belong to the pregroup.')
				
		for _tuple in self.Pregroup_operation:
			if _tuple[0][0] == a and _tuple[0][1] == b:
				return _tuple[1]

	def isPregroupAssociative(self, Printing_flag = False):
		'''
		Returns a boolean stating whether or not the Pregroup's
		operation is associative or not.

		We verify that (xy)z = x(yz) for every x,y and z in the set.

		-Printing_flag: a Boolean value which determines whether the
		script prints out every non-associative 3-tuple.
		'''
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

	def isPregroupModulative(self, Printing_flag = False):
		'''
		Returns a boolean: True if the Pregroup is modulative and
		False if the pregroup isn't.

		To check whether a pregroup is modulative or not, we verify that
		there exists an element that leaves others unchanged and that said
		element works for every element in the set.

		-Printing_flag: is a boolean that determines whether the module
		is printed on-screen.
		'''
		Module_flag = False
		for element in self.Pregroup_set:
			for _tuple in self.Pregroup_operation:
				if _tuple[0][0] == element and _tuple[1] == element:
					Module_flag = True
					Module = _tuple[0][1]

		if Module_flag:
			Counter_of_changed_elements = 0
			for element in self.Pregroup_set:
				a = self.operate(element,Module)
				b = self.operate(Module, element)
				if element != a or element != b:
					Counter_of_changed_elements += 1
			if Counter_of_changed_elements > 0:
				return False
			else:
				if Printing_flag:
					print('Module: ' + str(Module))
				return True
		else:
			return False

	def getModule(self):
		'''
		Returns the module of the operation, if the operation is
		modulative.

		To get the module, we first check if the pregroup is indeed
		modulative, once it is modulative (and because we know a-priori
		that the module is unique), we get one element that satisfies
		the definition.
		'''
		if self.isPregroupModulative(False):
			for element in self.Pregroup_set:
				for _tuple in self.Pregroup_operation:
					if _tuple[0][0] == element and _tuple[1] == element:
						Module_flag = True
						Module = _tuple[0][1]
			return Module
		else:
			raise RuntimeError('Pregroup is not modulative')

	def isPregroupInvertible(self):
		'''
		Returns a boolean: True if the Pregroup's operation is invertible
		and False if the Pregroup's operation isn't. 
		'''
		if self.isPregroupModulative(False):
			List_of_inverses = []
			e = self.getModule()
			for element1 in self.Pregroup_set:
				for element2 in self.Pregroup_set:
					if self.operate(element1, element2) == e:
						List_of_inverses.append((element1, element2))

			Not_inversible_element_flag = False
			for element in self.Pregroup_set:
				appearences_of_element = 0
				for _tuple in List_of_inverses:
					if _tuple[0] == element or _tuple[1] == element:
						appearences_of_element += 1
				if appearences_of_element == 0:
					Not_inversible_element_flag = True
					
			return not Not_inversible_element_flag
		else:
			print('The pregroup is not even modulative')
			return False

	def getInverse(self, element):
		'''
		Returns the inverse of an element, if it exists.

		This functions creates the set of inverses and gets one of the
		inverses (which, by our theory, should be unique).

		TODO:
		- What if there's a set with only a couple invertible elements?
		'''
		if element not in self.Pregroup_set:
			raise ValueError('Element is not in group')

		if self.isPregroupInvertible():
			List_of_inverses = []
			e = self.getModule()
			for element1 in self.Pregroup_set:
				for element2 in self.Pregroup_set:
					if self.operate(element1, element2) == e:
						List_of_inverses.append((element1, element2))
			for _tuple in List_of_inverses:
				if _tuple[0] == element:
					return _tuple[1]
		else:
			raise RuntimeError('Pregroup is not invertible')

	def isPregroupConmutative(self):
		'''
		Returns a boolean which states whether or not the Pregroup is
		conmutative.
		'''
		for element1 in self.Pregroup_set:
			for element2 in self.Pregroup_set:
				if self.operate(element1, element2) == self.operate(element2, element1):
					return True
				else:
					return False


class Group:
	'''
	A group object takes a set of elements and an operation. The set S =_set
	is a normal python set, and the operation is a set of tuples in which
	the first element is a tuple of elements of S in and the second is an
	element from S, that is, a tuple ((a,b), c) implies that a*b = c in
	the group.

	TO-DO:  
	- Create a function that generates (Zn, +) and other usual groups
	  -- Create an arithmetic on Zn which recognizes equivalence classes
	- Is it possible to work with infinite groups?
	- Think bigger: group actions and permutations
	'''
	
	def __init__(self, _set, _operation):
		self.Group_set = _set
		self.Group_operation = _operation

		G = Pregroup(_set, _operation)
		if not G.isPregroupAssociative() or not G.isPregroupModulative or not G.isPregroupInvertible:
			raise ValueError('The set with said operation is not a group')

	def getGroupSet(self):
		'''
		Returns the underlying set of the group.
		'''
		return self.Group_set

	def getGroupOrder(self):
		'''
		Returns the amount of elements in the underlying set
		of the group.
		'''
		return len(self.Group_set)

	def operate(self, a, b):
		'''
		Returns the result of operating a and b in that order. The
		elements a and b must belong to the group.
		'''
		if a in self.Group_set and b in self.Group_set:
			pass
		else:
			raise ValueError('Objects must belong to the group.')
			
		for _tuple in self.Group_operation:
			if _tuple[0][0] == a and _tuple[0][1] == b:
				return _tuple[1]

	def printGroupTable(self, string='*'):
		'''
		Prints the group's table operation.
		TO-DO:
		-Create a similar function that outputs this into a file.
		'''
		print(str(string) +' | ', end='')
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
		'''
		Returns a boolean: True if the group is abelian and False if
		the group isn't.
		'''
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

	def isGroupConmutative(self):
		'''
		Returns True if the group is abelian and False if it isn't.
		'''
		return self.isGroupAbelian()

	def getModule(self):
		'''
		Returns the module of the group.
		'''
		for element in self.Group_set:
			for _tuple in self.Group_operation:
				if _tuple[0][0] == element and _tuple[1] == element:
					Module = _tuple[0][1]
		return Module

	def getInverse(self, element):
		'''
		Returns the inverse of an element.
		'''
		if element not in self.Group_set:
			raise ValueError('Element is not in the group.')
		List_of_inverses = []
		e = self.getModule()
		for element1 in self.Group_set:
			for element2 in self.Group_set:
				if self.operate(element1, element2) == e:
					List_of_inverses.append((element1, element2))
		for _tuple in List_of_inverses:
			if _tuple[0] == element:
				return _tuple[1]

