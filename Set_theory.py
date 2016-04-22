'''
Set_theory.py, by MGD.

This library divides itself in two main parts:
 - Work with relations.
 - Work with finite functions.
'''

'''
Work with relations:
there's little to do with relations defined on AxB with A and B
different sets. We focus on determing whether a relation in a set
is of order, or of equivalence.

TO-DO:
- Organize the returns so that they result more legible.
- The work with lists is useless, we could always work with sets using
  emptyset = set([]) and replacing .append with .add.
- If _relation is empty, everything should hold up, but will it?
- Implement a function that returns the minimal domain (codomain) of
  a relation.
- Implement getQuotientSet of an equivalence relation.
- There's much to do with orders: get minimals, maximals, lower bounds
  upper bounds, ...
- Implement getHasseDiagram of an order relation.
'''
import csv

def isRelation(domain, codomain, _relation):
	'''
	Returns a boolean: True if relation is well defined, False otherwise.
	'''
	# Sanity check
	if type(_relation) != type({0,1}):
		raise ValueError('Relation must be a set.')

	if type(domain) != type({0,1}):
		raise ValueError('Domain must be a set.')

	if type(codomain) != type({0,1}):
		raise ValueError('Codomain must be a set.')

	for _tuple in _relation:
		if type(_tuple) != type((0,1)):
			raise ValueError('Relation must contain 2-tuples')

	# Checking whether every tuple in the relation is defined on AxB
	for _tuple in _relation:
		if _tuple[0] not in domain or _tuple[1] not in codomain:
			return False

	return True


def isRelationReflexive(_set, _relation):
	'''
	Returns a boolean: True if relation is reflexive, False otherwise.
	'''
	# Checking on the relation being indeed a relation.
	if not isRelation(_set, _set, _relation):
		raise ValueError('Argument is not a relation')

	# Checking if all elements belong to the diagonal.
	List_of_diagonal_elements = []
	for _tuple in _relation: 
		if _tuple[0] == _tuple[1]:
			List_of_diagonal_elements.append(_tuple[0])

	if set(List_of_diagonal_elements) == _set:
		return True
	elif set(List_of_diagonal_elements) != _set:
		return False

def isRelationSymmetric(_set, _relation):
	'''
	Returns a boolean: True if relation is symmetric, False otherwise.
	'''
	if not isRelation(_set, _set, _relation):
		raise ValueError('Argument is not a relation')
	
	for _tuple in _relation:
		if (_tuple[1], _tuple[0]) not in _relation:
			return False

	return True

def isRelationAntisymmetric(_set, _relation):
	'''
	Returns a boolean: True if relation is antisymmetric, False otherwise.
	'''
	if not isRelation(_set, _set, _relation):
		raise ValueError('Argument is not a relation')

	for _tuple in _relation:
		if (_tuple[1], _tuple[0]) in _relation and _tuple[0] != _tuple[1]:
			return False

	return True

def isRelationTransitive(_set, _relation):
	'''
	Returns a boolean: True if relation is transitive, False otherwise.
	'''
	if not isRelation(_set, _set, _relation):
		raise ValueError('Argument is not a relation')

	for _tuple1 in _relation:
		for _tuple2 in _relation:
			if _tuple1[1] == _tuple2[0]:
				if (_tuple1[0], _tuple2[1]) not in _relation:
					return False

	return True

def isRelationEquivalence(_set, _relation):
	'''
	Returns a boolean: True if relation is of equivalence, False otherwise.
	'''
	if not isRelation(_set, _set, _relation):
		raise ValueError('Argument is not a relation')

	if isRelationReflexive(_set, _relation):
		if isRelationSymmetric(_set, _relation):
			if isRelationTransitive(_set, _relation):
				return True

	return False

def getEquivalenceClass(_set, _relation, element):
	'''
	Returns the equivalence class of the element. Relation
	must be of equivalence.
	'''
	if not isRelationEquivalence(_set, _relation):
		raise ValueError('Relation must be of equivalence')

	for _tuple in _relation:
		if _tuple[0] == element:
				Equivalence_class_of_element.add(_tuple[1])
			if _tuple[1] == element:
				Equivalence_class_of_element.add(_tuple[0])

	return Equivalence_class_of_element

def getQuotientSet(_set, _relation):
	'''
	Returns the list of equivalence classes of the relation. Relation
	must be of equivalence. It can't return a set, for set objects are
	unhashable.
	'''
	if not isRelationEquivalence(_set, _relation):
		raise ValueError('Relation must be of equivalence')

	Quotient_list = []
	for element in _set:
		Equivalence_class_of_element = getEquivalenceClass(_set, _relation, element)
		Quotient_list.append(Equivalence_class_of_element)

	return Quotient_list

def isRelationOrder(_set, _relation):
	'''
	Returns a boolean: True if relation is an order, False otherwise.
	'''
	if not isRelation(_set, _set, _relation):
		raise ValueError('Argument is not a relation')

	if isRelationReflexive(_set, _relation):
		if isRelationAntisymmetric(_set, _relation):
			if isRelationTransitive(_set, _relation):
				return True

	return False

'''
Work with finite functions:
we determine whether a function is injective, surjective or bijective.
'''

def isRelationFunction(domain, codomain, _relation):
	'''
	Returns a boolean, stating whether a given relation is a
	function or not.
	'''
	if not isRelation(domain, codomain, _relation):
		raise ValueError('Argument must be a relation')

	for element in domain:
		list_of_tuples_with_element_as_first =[]
		for _tuple in _relation:
			if _tuple[0] == element:
				list_of_tuples_with_element_as_first.append(_tuple)
		if list_of_tuples_with_element_as_first == []:
			return False
		if len(list_of_tuples_with_element_as_first) > 1:
			return False

	return True

def isFunctionInjective(domain, codomain, _function):
	'''
	Returns a boolean, stating whether or not the function is injective.
	'''
	if not isRelation(domain, codomain, _function):
		raise ValueError('Function must first be a relation')

	if not isRelationFunction(domain, codomain, _function):
		raise ValueError('The argument that was passed is not a function')

	for element in codomain:
		list_of_tuples_with_element_as_second = []
		for _tuple in _function:
			if _tuple[1] == element:
				list_of_tuples_with_element_as_second.append(_tuple)
		if len(list_of_tuples_with_element_as_second) == 0:
			pass
		elif len(list_of_tuples_with_element_as_second) > 1:
			return False

	return True

def isFunctionSurjective(domain, codomain, _function):
	'''
	Returns a boolean, stating whether or not the function is surjective.
	'''
	if not isRelation(domain, codomain, _function):
		raise ValueError('Function must first be a relation')
	
	if not isRelationFunction(domain, codomain, _function):
		raise ValueError('The argument that was passed is not a function')

	for element in codomain:
		list_of_tuples_with_element_as_second = []
		for _tuple in _function:
			if _tuple[1] == element:
				list_of_tuples_with_element_as_second.append(_tuple)
		if len(list_of_tuples_with_element_as_second) == 0:
			return False

	return True

def isFunctionBijective(domain, codomain, _function):
	'''
	Returns a boolean, stating whether or not the function is bijective.
	'''
	if not isRelation(domain, codomain, _function):
		raise ValueError('Function must first be a relation')
	
	if not isRelationFunction(domain, codomain, _function):
		raise ValueError('The argument that was passed is not a function')

	if isFunctionInjective(domain, codomain, _function) and isFunctionSurjective(domain, codomain, _function):
		return True

	return False

def getRelationFromCSV(file_name):
	'''
	Returns a 3-tuple: (domain, codomain, relation)
	'''
	file_csv = csv.reader(open(file_name), delimiter = ' ')
	file_matrix = []
	for row in file_csv:
		file_matrix.append(row)
		if len(row) != 2:
			raise ValueError('File must contain a pair of elements per row')
	_relation_list = []
	_domain_list = []
	_codomain_list = []
	for row in file_matrix:
		_domain_list.append(row[0])
		_codomain_list.append(row[1])
		element = (row[0], row[1])
		_relation_list.append(element)

	_domain = set(_domain_list)
	_codomain = set(_codomain_list)
	_relation = set(_relation_list)

	return (_domain, _codomain, _relation)

def getFunctionFromCSV(file_name):
	'''
	Returns a 3-tuple: (domain, codomain, function)
	'''
	file_csv = csv.reader(open(file_name), delimiter = ' ')
	file_matrix = []
	for row in file_csv:
		file_matrix.append(row)
		if len(row) != 2:
			raise ValueError('File must contain a pair of elements per row')
	_relation_list = []
	_domain_list = []
	_codomain_list = []
	for row in file_matrix:
		_domain_list.append(row[0])
		_codomain_list.append(row[1])
		element = (row[0], row[1])
		_relation_list.append(element)

	_domain = set(_domain_list)
	_codomain = set(_codomain_list)
	_relation = set(_relation_list)

	if not isRelationFunction(_domain, _codomain, _relation):
		raise ValueError('Relation is not a function')

	return (_domain, _codomain, _relation)