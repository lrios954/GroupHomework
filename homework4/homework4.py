import os
import numpy
import sys
import pylab
import scipy
from scipy.optimize import curve_fit
from scipy.linalg import eigh

table = []
theta = []
var_gravity = []
avg_grav = []
pca = []
data = open('data.dat', 'a')

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
	table.append((int(name[1]),float(name[3]),float(x_reg[0]),float(y_reg[1]),(-2.0*float(y_reg[0]))))
	# el formato es: [ID, angulo, v_0_x, v_0_y, g]


# Organiza los datos en orden creciente respecto al angulo
table.sort(key=lambda tup: tup[1])

# imprime la lista con la informacion de los experimentos
data.write('\n'.join('%f %f %f %f %f' % x for x in table))

print 'information exported sucessfully in data.dat'

for line in table:

	theta.append(line[1])
	pca.append(repr(line[2])+' '+repr(line[3])+' '+repr(line[4]))


n_dimensions=3
n_measurements=len(pca)

data=numpy.empty((n_dimensions,n_measurements,))

for i in range(n_measurements):

    datosLinea=pca[i].split()

    for j in range(n_dimensions):
        
        datosLinea[j]=float(datosLinea[j])
        data.itemset((j,i),datosLinea[j])

covariance_matrix=numpy.cov(data)

w,u = eigh(covariance_matrix, overwrite_a = True)

#Imprime los valores y vectores propios en orden descendente de valores propios en el archivo results_pca.dat

out_name='results_pca.dat'
out=open(out_name,'w')
out.write('Eigenvalues:')
out.write('\n')
out.write(''.join('%s' % w[::-1]))
out.write('\n')
out.write('Eigenvectors:')
out.write('\n')
out.write(''.join('%s' % u[:,::-1]))
out.close()

print 'PCA results exported sucessfully in results_pca.dat'

angles = list(set(theta))

# calcula la gravedad media para cada angulo
for angle in angles:
	
	partial = 0.0
	
	for line in table:
	
		if (line[1] == angle) :
		
			partial += line[4]
			
	partial /= 6.0
	avg_grav.append(partial)
	
# grafica gravedad media vs angulo y lo guarda en el archivo 'gravityplot.png' 
pylab.plot(angles, avg_grav, '.')
pylab.xlabel('angle (degrees)')
pylab.ylabel('average gravity (m/s)')
pylab.title('Average gravity vs Angle')
pylab.savefig('gravityplot')
pylab.grid(True)

pylab.show()

print 'gravityplot.png written sucessfully'


# calcula variaciones de la gravedad
for i in range(len(avg_grav)):

	var_gravity.append(1-(avg_grav[i]/(9.81)))

# hace un fit de los datos
def f(x, a, b):
     return a*numpy.sin(numpy.deg2rad(x)) + b

parameters = (scipy.optimize.curve_fit(f, numpy.array(angles), numpy.array(var_gravity)))[0]

pylab.plot(angles, f(angles,parameters[0],parameters[1]), '.')
pylab.plot(angles, var_gravity, '.')
pylab.xlabel('angle (degrees)')
pylab.ylabel('gravitational variation (dimensionless)')
pylab.title('Gravitational Variation vs angle')
pylab.grid(True)
pylab.show()

# grafica residuo vs angulo y lo guarda en el archivo 'residueplot.png' 
pylab.plot(angles, f(angles,parameters[0],parameters[1])-var_gravity, '.')
pylab.xlabel('angle (degrees)')
pylab.ylabel('residue (dimensionless)')
pylab.title('Residue vs angle')
pylab.savefig('residueplot')
pylab.grid(True)
pylab.show()

print 'residueplot.png written sucessfully'
