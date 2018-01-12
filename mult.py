# Create a program that prints a multiplication table in your console.
def multiplication_table():
	print 'x', '\t', '1', '\t', '2', '\t', '3', '\t', '4', '\t', '5','\t', '6','\t', '7','\t', '8','\t', '9','\t', '10','\t', '11','\t', '12', '\n'
	# "'\t', " tabs and spaces out the numbers,"'\n', " creates  new line 
	for table in range(1,13):
		for line in range(1, 13):
			if line == 1:
				print table, '\t',
			print table*line, '\t', 
		print 

multiplication_table()