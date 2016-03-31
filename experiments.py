import Group_theory as GT

def main():
	_set = {0,1}
	_operation = {((0,0),0),
				  ((0,1),1),
				  ((1,0),1),
				  ((1,1),0)}
	# G = GT.Group(_set, _operation)
	# print('Order: ' + str(G.getGroupOrder()))
	# print('Underlying set: ' + str(G.getGroupSet()))
	# print(type(G.getGroupOrder()))
	# G.printGroupTable()
	# print(G.operate(0,0))
	# print(G.isGroupAbelian())
	# print()

	PG = GT.Pregroup(_set, _operation)

	PG.printPregroupTable('+')
	print(PG.isPregroupAssociative(True))

	Vector_set = {' i', ' j', ' k', '-i', '-j', '-k', ' 0'}
	Vector_times = {((' i', ' i'), ' 0'),
					((' i', ' j'), ' k'),
					((' i', ' k'), '-j'),
					((' i', '-i'), ' 0'),
					((' i', '-j'), '-k'),
					((' i', '-k'), ' j'),
					((' i', ' 0'), ' 0'),
					((' j', ' i'), '-k'),
					((' j', ' j'), ' 0'),
					((' j', ' k'), ' i'),
					((' j', '-i'), ' k'),
					((' j', '-j'), ' 0'),
					((' j', '-k'), '-i'),
					((' j', ' 0'), ' 0'),
					((' k', ' i'), ' j'),
					((' k', ' j'), '-i'),
					((' k', ' k'), ' 0'),
					((' k', '-i'), '-j'),
					((' k', '-j'), ' i'),
					((' k', '-k'), ' 0'),
					((' k', ' 0'), ' 0'),
					(('-i', ' i'), ' 0'),
					(('-i', ' j'), '-k'),
					(('-i', ' k'), ' j'),
					(('-i', '-i'), ' 0'),
					(('-i', '-j'), ' k'),
					(('-i', '-k'), '-j'),
					(('-i', ' 0'), ' 0'),
					(('-j', ' i'), ' k'),
					(('-j', ' j'), ' 0'),
					(('-j', ' k'), '-i'),
					(('-j', '-i'), '-k'),
					(('-j', '-j'), ' 0'),
					(('-j', '-k'), ' i'),
					(('-j', ' 0'), ' 0'),
					(('-k', ' i'), '-j'),
					(('-k', ' j'), ' i'),
					(('-k', ' k'), ' 0'),
					(('-k', '-i'), ' j'),
					(('-k', '-j'), '-i'),
					(('-k', '-k'), ' 0'),
					(('-k', ' 0'), ' 0'),
					((' 0', ' i'), ' 0'),
					((' 0', ' j'), ' 0'),
					((' 0', ' k'), ' 0'),
					((' 0', '-i'), ' 0'),
					((' 0', '-j'), ' 0'),
					((' 0', '-k'), ' 0'),
					((' 0', ' 0'), ' 0'),
					}
	Vector_pregroup = GT.Pregroup(Vector_set, Vector_times)

	Vector_pregroup.printPregroupTable(' X')
	if Vector_pregroup.isPregroupAssociative(False):
		print('is associative.')
	else:
		print('Pregroup is not associative')

	Bad_operation = {((0,0),0),
				     ((0,1),1),
				  	 ((1,1),0)}

	G = GT.Group(_set, Bad_operation)

if __name__ == '__main__':
	main()