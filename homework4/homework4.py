
import os
import numpy
import sys
import pylab

table = []
gravity = []
theta = []

# corre un loop en el directorio hw4_data
for filename in os.listdir('hw4_data/' ):
	
        info = []
        t_data = []
        x_data = []
        y_data = []
	name = (filename.replace('.dat','')).split('_')

	# inicializa el path del archivo
	path = os.path.expanduser('hw4_data/' + filename)
	
	# lee el archivo
	info0 = open(path, 'r').readlines()
	
	# le da el formato correcto a la informacion dentro del archivo
	for line in info0:

		info.append(line.split())
			
	info.pop(0)
	info.remove(['#', '[second]', '[meter]', '[meter]'])
	for line in info:
		
		t_data.append(float(line[0]))
		x_data.append(float(line[1]))
		y_data.append(float(line[2]))
	
	# hace un fit de los datos de 'x' y 'y'	
	x_reg = numpy.polyfit(numpy.array(t_data), numpy.array(x_data), 1.0)
	y_reg = numpy.polyfit(numpy.array(t_data), numpy.array(y_data), 2.0)

	# agrega a la lista una tupla con la informacion del archivo
	table.append((float(name[1]),float(name[3]),float(x_reg[0]),float(y_reg[1]),(2.0*float(y_reg[0]))))
	# el formato es: [ID, angulo, v_0_x, v_0_y, g]

# imprime la lista con la informacion de los experimentos
for line in table:
	
	print line
	theta.append(line[1])
	gravity.append(line[4])

# grafica aceleracion vs angulo y lo guarda en el archivo 'gravityplot.png' 
pylab.plot(theta, gravity, '+')
pylab.xlabel('angle (degrees)')
pylab.ylabel('acceleration (m/s)')
pylab.title('Acceleration vs Angle')
pylab.savefig('gravityplot')
pylab.grid(True)
pylab.show()

