'''
Group_theory.py, by MGD.

In this file, the main objects of group theory are defined:
- A pregroup is a set with an operation, said operation may not even be
  associative, nor modulative or inverible. But it does have to be
  defined on the set that is passed. 
- A group is a set with an operation that is indeed associative,
  modulative and invertible.
For more information, check the documentation of each object.
'''

'''
TO-DO:
 - Create group actions.
 - Implement getNonInversibleElements().
'''

import Set_theory as ST
import csv

class Pregroup:
	'''
	A Pregroup is just a set with an operation. The operation doesn't
	need to be associative, modulative or invertive. Once those three
	conditions are satisfied, a Pregroup can be also called as a group.
	The set S = _set that the Pregroup object takes is a normal python set,
	and the operation is a set of tuples of the form ((a,b), c) which
	implies a*b=c, the operation must have for every pair of elements of S
	the value of their operation. Otherwise an error is raised.

	There's an easier way of importing a Pregroup, and that is by
	using the getPregroupFromCSV function, which takes as an argument
	the name of a file which contains the table of the operation.

	This class commes with functions that determine whether or not the 
	operation is associative, modulative or invertive.
	'''

	def __init__(self, _set, _operation):
		self.Pregroup_set = _set
		self.Pregroup_operation = _operation

		# Checking if arguments are indeed a sets
		if type(self.Pregroup_set) != set or type(self.Pregroup_operation) != set:
			raise ValueError('Both arguments should be sets.')

		# Checking if the operation is correctly defined
		for _tuple in self.Pregroup_operation:
			if _tuple[0][0] not in self.Pregroup_set:
				raise ValueError('Elements in operation should belong to the set.')
			if _tuple[0][1] not in self.Pregroup_set:
				raise ValueError('Elements in operation should belong to the set.')
			if _tuple[1] not in self.Pregroup_set:
				raise ValueError('Elements in operation should belong to the set.')

		_domain_list = []
		for element1 in self.Pregroup_set:
			for element2 in self.Pregroup_set:
				_domain_list.append((element1, element2))
		_domain = set(_domain_list)

		# Checking if the operation is a function from GxG to G. 
		if not ST.isRelationFunction(_domain, self.Pregroup_set, _operation):
			raise ValueError('Operation is not a function.')

	def getPregroupSet(self):
		'''
		Returns the underlying set of the Pregroup.
		'''
		return self.Pregroup_set

	def getPregroupOperation(self):
		'''
		Returns the underlying operation of the Pregroup.
		'''
		return self.Pregroup_operation

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
		TO-DO: 
		 - Fix spaces depending on how big the elements in the set are.
		 - Perhaps use the getTable functions in some way.
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
		if self.isPregroupModulative():
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
		if self.isPregroupModulative():
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
		'''

		'''
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

	def isPregroupGroup(self):
		'''
		Returns a boolean: True if the operation is associative, modulative
		and invertible, False otherwise.
		'''
		return self.isPregroupAssociative() and self.isPregroupModulative() and self.isPregroupInvertible()

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

		if type(self.Group_set) != set or type(self.Group_operation) != set:
			raise ValueError('Both arguments should be sets.')

		G = Pregroup(_set, _operation)
		if not G.isPregroupGroup:
			raise ValueError('The set with said operation is not a group')

	def getGroupSet(self):
		'''
		Returns the underlying set of the group.
		'''
		return self.Group_set

	def getGroupOperation(self):
		'''
		Returns the underlying set of the group.
		'''
		return self.Group_operation

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
		if a  not in self.Group_set or b not in self.Group_set:
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

	def getSubgroupGeneratedBy(self, subset):
		'''
		Returns the underlying set of the subgroup generated by the
		given subset.

		This algorithm was invented by math.stackexchange user Hagen
		von Eitzen on question 1758649.
		'''
		if type(subset) != set:
			raise ValueError('Argument must be a set')

		for element in subset:
			if element not in self.Group_set:
				raise ValueError('Argument must be a subset of the Group')

		Subgroup = []
		Queue_list = []
		Queue_list.append(self.getModule())

		while Queue_list != []:
			q = Queue_list.pop()
			if q not in Subgroup:
				Subgroup.append(q)
				for element in subset:
					Queue_list.append(operate(q,element))

		return Subgroup

#Other functions

#Creating a Zn

def getZn(n):
	'''
	Returns the abelian group Zn, n must be a positive integer.
	'''
	if type(n) != type(1) or n<0:
		raise ValueError('n must be a positive integer.')

	_set = set(range(n))
	_operation = []
	for element1 in _set:
	    for element2 in _set:
	        _tuple = (element1, element2)
	        _operation.append((_tuple, (element1+element2)% n))
	return Group(_set, set(_operation))

def getPregroupFromCSV(file_name):
	'''
	Returns a pregroup from a csv file. Delimiters must be white
	spaces.
	'''
	file_csv = csv.reader(open(file_name), delimiter = ' ')
	file_matrix = []
	for row in file_csv:
		file_matrix.append(row)
	order = len(file_matrix)

	for row in file_matrix:
		if len(row) != order:
			raise ValueError('The csv file must form a square matrix')

	_operation_list = []
	for i in range(1, len(file_matrix)): 
	    for j in range(1, len(file_matrix)):
	        element = ((file_matrix[i][0], file_matrix[0][j]), file_matrix[i][j])
	        _operation_list.append(element)

	_domain_list = []
	for element in file_matrix[0]:
		if element != '*':
			_domain_list.append(element)

	return Pregroup(set(_domain_list), set(_operation_list))

def getGroupFromCSV(file_name):
	'''
	Returns a group from a csv file. Delimiters must be white spaces.
	'''
	_Pregroup = getPregroupFromCSV(file_name)
	if _Pregroup.isPregroupGroup():
		return Group(_Pregroup.getPregroupSet(), _Pregroup.getPregroupOperation())

