import Group_theory as GT

Z2 = GT.Group({0, 1}, {((0,0),0),((0,1),1),((1,0),1),((1,1),0)})

def test_group_order_is_consistent():
	assert Z2.getGroupOrder() == 2

def test_group_set_is_consistent():
	assert Z2.getGroupSet() == {0, 1}

def test_Z2_is_abelian():
	assert Z2.isGroupAbelian()
