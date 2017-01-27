#composing a string from a document

#WARNING: DONOT do this! String is immutatble and this is inefficient ~ O(n^2)

var s = ''

for c in document:
	s += c


#this is faster with a guaranteed O(n) runtime

s = ''
var temp = []

for c in document:
	temp.append(c)

s = ''.join(temp);

#initializing a multi dimentional array. m * n matrix

x = [[0] * n for j in range(m)] # correct with m dirrent lists 

x = [[0] * n] * m 				# wrong because all m lists refer to same list and doing things like x[0][2] = 1 will change entire column instead on single element


