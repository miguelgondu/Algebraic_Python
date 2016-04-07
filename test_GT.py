import Group_theory as GT
import Set_theory as ST

Z2 = GT.Group({0, 1}, {((0,0),0),((0,1),1),((1,0),1),((1,1),0)})

_domain = {0,1}
_function = {(0,0), (1,1)}
_not_a_function1 = {(0,0), (0,1)}
_not_a_function2 = {(0,0)}
_injective_function = {(0,1), (1,0)}
_not_injective_function = {(0,0), (1,0)}
_surjective_function = {(0,1), (1,0)}
_not_surjective_function = {(0,0), (1,0)}


def test_group_order_is_consistent():
	assert Z2.getGroupOrder() == 2

def test_group_set_is_consistent():
	assert Z2.getGroupSet() == {0, 1}

def test_Z2_is_abelian():
	assert Z2.isGroupAbelian()

def test_is_function():
	assert ST.isRelationFunction(_domain, _domain, _function)

def test_is_not_a_function1():
	assert not ST.isRelationFunction(_domain, _domain, _not_a_function1)

def test_is_not_a_function2():
	assert not ST.isRelationFunction(_domain, _domain, _not_a_function2)

def test_is_injective():
	assert ST.isFunctionInjective(_domain, _domain, _injective_function)

def test_is_not_injective():
	assert not ST.isFunctionInjective(_domain, _domain, _not_injective_function)

def test_is_surjective():
	assert ST.isFunctionSurjective(_domain, _domain, _surjective_function)

def test_is_not_surjective():
	assert not ST.isFunctionSurjective(_domain, _domain, _not_surjective_function)

def test_is_bijective():
	assert ST.isFunctionBijective(_domain, _domain, _function)
