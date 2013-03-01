import os
import numpy
import sys
table = []

for filename in os.listdir('hw4_data/' ):
	
	name = (filename.replace('.dat','')).split('_')
	
	path = os.path.expanduser('hw4_data/' + filename)
	
	info0 = open(path, 'r').readlines()
	
	info = []
	t_data = []
	x_data = []
	y_data = []
	for line in info0:
	
		info.append(line.split())
			
	info.pop(0)
	info.remove(['#', '[second]', '[meter]', '[meter]'])
	for line in info:
		
		t_data.append(float(line[0]))
		x_data.append(float(line[1]))
		y_data.append(float(line[2]))
		
	x_reg = numpy.polyfit(numpy.array(t_data), numpy.array(x_data), 1.0)
	y_reg = numpy.polyfit(numpy.array(t_data), numpy.array(y_data), 2.0)
	# print (info)

	table.append((float(name[1]),float(name[3]))+tuple(x_reg)+tuple(y_reg))
	
# print ('\n'.join('%f %f %f %f %f %f %f' % x for x in table))

for line in table:

	print (line)
	print '\n'

		
