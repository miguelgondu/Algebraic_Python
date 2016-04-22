import Group_theory as GT
import Set_theory as ST
import csv

'''
TO-DO:
- Implement even more examples with domain different from codomain.
'''

Z2 = GT.Group({0, 1}, {((0,0),0),((0,1),1),((1,0),1),((1,1),0)})

# Manual testing
_domain = {0,1}
_codomain = {0,1,2}
_relation_on_domain_codomain = {(0,1), (0,2), (1,1)}
_not_a_relation_on_domain_codomain = {(2,1), (0,0)}
_reflexive_relation_on_domain = {(0,0), (1,1), (0,1)}
_not_a_reflexive_relation_on_domain = {(0,0), (0,1)}
_symmetric_relation_on_domain = {(0,1), (0,0), (1,0)}
_not_a_symmetric_relation_on_domain = {(0,1), (0,0)}
_antisymmetric_relation_on_domain = {(0,0), (0,1)}
_not_an_antisymmetric_relation_on_domain = {(0,1), (1,0)}
_transitive_relation_on_domain = {(0,0), (0,1), (1,0), (1,1)}
_not_a_transitive_relation_on_domain = {(0,1), (1,0)}
_function = {(0,0), (1,1)}
_not_a_function1 = {(0,0), (0,1)}
_not_a_function2 = {(0,0)}
_injective_function = {(0,1), (1,0)}
_not_injective_function = {(0,0), (1,0)}
_surjective_function = {(0,1), (1,0)}
_not_surjective_function = {(0,0), (1,0)}
Z5 = GT.getZn(5)

def test_group_order_is_consistent():
	assert Z2.getGroupOrder() == 2

def test_group_set_is_consistent():
	assert Z2.getGroupSet() == {0, 1}

def test_Z2_is_abelian():
	assert Z2.isGroupAbelian()

def test_Z2s_module():
	assert Z2.getModule() == 0

def test_Z5s_inverse():
	assert Z5.getInverse(3) == 2

def test_is_relation():
	assert ST.isRelation(_domain,_codomain,_relation_on_domain_codomain)

def test_is_not_a_relation():
	assert not ST.isRelation(_domain,_codomain, _not_a_relation_on_domain_codomain)

def test_is_reflexive_relation():
	assert ST.isRelationReflexive(_domain, _reflexive_relation_on_domain)

def test_is_not_a_reflexive_relation():
	assert not ST.isRelationReflexive(_domain, _not_a_reflexive_relation_on_domain)

def test_is_symmetric_relation():
	assert ST.isRelationSymmetric(_domain, _symmetric_relation_on_domain)

def test_is_not_a_symmetric_relation():
	assert not ST.isRelationSymmetric(_domain, _not_a_symmetric_relation_on_domain)

def test_is_antisymmetric_relation():
	assert ST.isRelationAntisymmetric(_domain, _antisymmetric_relation_on_domain)

def test_is_not_an_antisymmetric_relation():
	assert not ST.isRelationAntisymmetric(_domain, _not_an_antisymmetric_relation_on_domain)

def test_is_transitive_relation():
	assert ST.isRelationTransitive(_domain, _transitive_relation_on_domain)

def test_is_not_an_transitive_relation():
	assert not ST.isRelationTransitive(_domain, _not_a_transitive_relation_on_domain)

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

#CSV testing:
def test_csv_not_a_function():
	A, B, f = ST.getRelationFromCSV("relation_not_a_function.csv")
	assert not ST.isRelationFunction(A, B, f)

def test_csv_works_on_functions():
	A, B, f = ST.getFunctionFromCSV("function.csv")
	assert ST.isRelationFunction(A, B, f)

def test_csv_works_on_pregroups():
	D3 = GT.getPregroupFromCSV("table_D_3.csv")

def test_csv_works_on_groups():
	D3 = GT.getGroupFromCSV("table_D_3.csv")
	assert not D3.isGroupAbelian()


