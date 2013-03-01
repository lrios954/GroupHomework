import os
import numpy

table = []

for filename in os.listdir('hw4_data/' ):
	
	name = (filename.replace('.dat','')).split('_')
	
	path = os.path.expanduser('hw4_data/' + filename)
	
	filein = open(path, 'r')
	
	
	print data
	
	table.append((name[1],name[3]))
	
table.sort()
	
print ('\n'.join('%s %s' % x for x in table))

	
