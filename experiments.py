import Group_theory as GT

def main():

	Z3_set = {0,1,2}
	Z3_operation = {((0,0), 0),
					((0,1), 1),
					((0,2), 2),
					((1,0), 1),
					((1,1), 2),
					((1,2), 0),
					((2,0), 2),
					((2,1), 0),
					((2,2), 1)
					}

	Z3 = GT.Pregroup(Z3_set, Z3_operation)
	Z3.printPregroupTable('+')
	print('About Z3 = ' + str(Z3_set) +' we can answer: ')
	print('Is Associative?: ' + str(Z3.isPregroupAssociative(False)))
	print('Is Modulative?: ' + str(Z3.isPregroupModulative(False)))
	print('Is Invertible?: ' + str(Z3.isPregroupInvertible()))
	print('Is Conmutative?: ' + str(Z3.isPregroupConmutative()))
	print('The inverse of 1 is: ' + str(Z3.getInverse(1)))

	Z3 = GT.Group(Z3_set, Z3_operation)
	
	#Vector_set = {' i', ' j', ' k', '-i', '-j', '-k', ' 0'}
	#Vector_times = {((' i', ' i'), ' 0'),
					#((' i', ' j'), ' k'),
					#((' i', ' k'), '-j'),
					#((' i', '-i'), ' 0'),
					#((' i', '-j'), '-k'),
					#((' i', '-k'), ' j'),
					#((' i', ' 0'), ' 0'),
					#((' j', ' i'), '-k'),
					#((' j', ' j'), ' 0'),
					#((' j', ' k'), ' i'),
					#((' j', '-i'), ' k'),
					#((' j', '-j'), ' 0'),
					#((' j', '-k'), '-i'),
					#((' j', ' 0'), ' 0'),
					#((' k', ' i'), ' j'),
					#((' k', ' j'), '-i'),
					#((' k', ' k'), ' 0'),
					#((' k', '-i'), '-j'),
					#((' k', '-j'), ' i'),
					#((' k', '-k'), ' 0'),
					#((' k', ' 0'), ' 0'),
					#(('-i', ' i'), ' 0'),
					#(('-i', ' j'), '-k'),
					#(('-i', ' k'), ' j'),
					#(('-i', '-i'), ' 0'),
					#(('-i', '-j'), ' k'),
					#(('-i', '-k'), '-j'),
					#(('-i', ' 0'), ' 0'),
					#(('-j', ' i'), ' k'),
					#(('-j', ' j'), ' 0'),
					#(('-j', ' k'), '-i'),
					#(('-j', '-i'), '-k'),
					#(('-j', '-j'), ' 0'),
					#(('-j', '-k'), ' i'),
					#(('-j', ' 0'), ' 0'),
					#(('-k', ' i'), '-j'),
					#(('-k', ' j'), ' i'),
					#(('-k', ' k'), ' 0'),
					#(('-k', '-i'), ' j'),
					#(('-k', '-j'), '-i'),
					#(('-k', '-k'), ' 0'),
					#(('-k', ' 0'), ' 0'),
					#((' 0', ' i'), ' 0'),
					#((' 0', ' j'), ' 0'),
					#((' 0', ' k'), ' 0'),
					#((' 0', '-i'), ' 0'),
					#((' 0', '-j'), ' 0'),
					#((' 0', '-k'), ' 0'),
					#((' 0', ' 0'), ' 0'),
					#}
	#Vector_pregroup = GT.Pregroup(Vector_set, Vector_times)

	Z5 = GT.getZn(5)
	print('Z5 = ' + str(Z5.getGroupSet()))
	Z5.printGroupTable('+')


if __name__ == '__main__':
	main()