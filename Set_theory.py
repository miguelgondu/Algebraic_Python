'''
Set_theory.py, by MGD.

Working with finite functions (presented by sets of tuples), we determine
whether a function is injective, surjective or bijective.
'''

def isRelationFunction(domain, codomain, _relation):
	if type(_relation) != type({0,1}):
		raise ValueError('Relation must be a set.')

	if type(domain) != type({0,1}):
		raise ValueError('Domain must be a set.')

	if type(codomain) != type({0,1}):
		raise ValueError('Codomain must be a set.')

	for _tuple in _relation:
		if type(_tuple) != type((0, 1)):
			raise ValueError('Relation must contain tuples.')

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
	if type(_function) != type({0,1}):
		raise ValueError('Function must be a set.')

	if type(domain) != type({0,1}):
		raise ValueError('Domain must be a set.')

	if type(codomain) != type({0,1}):
		raise ValueError('Codomain must be a set.')

	for _tuple in _function:
		if type(_tuple) != type((0,1)):
			raise ValueError('Function must contain tuples.')

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
	if type(_function) != type({0,1}):
		raise ValueError('Function must be a set.')

	if type(domain) != type({0,1}):
		raise ValueError('Domain must be a set.')

	if type(codomain) != type({0,1}):
		raise ValueError('Codomain must be a set.')

	for _tuple in _function:
		if type(_tuple) != type((0,1)):
			raise ValueError('Function must contain tuples.')

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
	if type(_function) != type({0,1}):
		raise ValueError('Function must be a set.')

	if type(domain) != type({0,1}):
		raise ValueError('Domain must be a set.')

	if type(codomain) != type({0,1}):
		raise ValueError('Codomain must be a set.')

	for _tuple in _function:
		if type(_tuple) != type((0,1)):
			raise ValueError('Function must contain tuples.')

	if not isRelationFunction(domain, codomain, _function):
		raise ValueError('The argument that was passed is not a function')

	if isFunctionInjective(domain, codomain, _function) and isFunctionSurjective(domain, codomain, _function):
		return True

	return False
