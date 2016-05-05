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
- There's much to do with orders: get minimals, maximals, lower bounds
  upper bounds, ...
- Implement getHasseDiagram of an order relation.
'''
import csv
from itertools import chain, combinations

'''
Work with sets in general:
'''

def getPowerSet(_set):
	'''
	Returns a list with the power set of a given set. Taken
	in part from the recipies in itertools' webpage: 
	https://docs.python.org/2/library/itertools.html#recipes
	'''
	if type(_set) != set:
		raise ValueError('Argument must be a set')

	s = list(_set)
	_powerset = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
	powerset = []
	for element in set(_powerset):
		powerset.append(set(element))

	return powerset


'''
Work with Relations:
'''

def isRelation(domain, codomain, _relation):
	'''
	Returns a boolean: True if relation is well defined, False otherwise.
	'''
	# Sanity check
	if type(_relation) != set:
		raise ValueError('Relation must be a set.')

	if type(domain) != set:
		raise ValueError('Domain must be a set.')

	if type(codomain) != set:
		raise ValueError('Codomain must be a set.')

	for _tuple in _relation:
		if type(_tuple) != tuple:
			raise ValueError('Relation must contain 2-tuples')

	# Checking whether every tuple in the relation is defined on AxB
	for _tuple in _relation:
		if _tuple[0] not in domain or _tuple[1] not in codomain:
			return False

	return True

def getDomainOfRelation(_relation):
	'''
	Returns the (minimal) domain of a given relation.
	'''
	_domain_list = []
	for _tuple in _relation:
		_domain_list.append(_tuple[0])

	return set(_domain_list)

def getRangeOfRelation(_relation):
	'''
	Returns the range of a given relation.
	'''
	_range_list = []
	for _tuple in _relation:
		_range_list.append(_tuple[1])

	return set(_range_list)

def getCompositionOfRelations(_relation1, _relation2):
	'''
	Returns the composition of the first argument and the second.
	The range of the first one must be contained in the domain of the
	second.
	'''
	_domain1 = getDomainOfRelation(_relation1)
	_range1 = getRangeOfRelation(_relation1)
	_domain2 = getDomainOfRelation(_relation2)

	if not _range1 <= _domain2:
		raise ValueError('The compsition cannot be made')

	_composition_list = []
	for _tuple1 in _relation1:
		for _tuple2 in _relation2:
			if _tuple1[1] == _tuple2[0]:
				_composition_list.append((_tuple1[0], _tuple2[1]))

	return set(_composition_list)


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

	Equivalence_class_of_element = set([])
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
		if Equivalence_class_of_element not in Quotient_list:
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

def getDomainOfFunction(_function):
	'''
	Returns the domain of a given function.
	'''
	_domain_list = []
	for _tuple in _function:
		_domain_list.append(_tuple[0])

	return set(_domain_list)

def getRangeOfFunction(_function):
	'''
	Returns the range of a given function.
	'''
	_range_list = []
	for _tuple in _function:
		_range_list.append(_tuple[1])

	return set(_range_list)

def getCompositionOfFunctions(_function1, _function2):
	'''
	Returns the composition of the functions.
	'''
	_domain1 = getDomainOfFunction(_function1)
	_range1 = getRangeOfFunction(_function1)
	_domain2 = getDomainOfFunction(_function2)
	_range2 = getRangeOfFunction(_function2)

	if not isRelationFunction(_domain1, _range1, _function1):
		raise ValueError('First argument is not a function')

	if not isRelationFunction(_domain2, _range2, _function2):
		raise ValueError('Second argument is not a function')

	return getCompositionOfRelations(_function1, _function2)

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
