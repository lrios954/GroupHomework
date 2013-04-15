import pylab
import numpy

print ' Python no es muy rapido graficando, por favor espere...'

for i in range(10):

	data = numpy.loadtxt(open(str(i)+'.dat', 'r'))
	x = data[:,1]
	y = data[:,2]
	z = data[:,3]
	
	pylab.plot(x, y, 'k')
	pylab.xlabel('x')
	pylab.ylabel('y')
	pylab.title(str(i)+' x-y')
	pylab.savefig(str(i)+'_x-y.jpg')
	pylab.close()

	pylab.plot(x, z, 'k')
	pylab.xlabel('x')
	pylab.ylabel('z')
	pylab.title(str(i)+' x-z')
	pylab.savefig(str(i)+'_x-z.jpg')
	pylab.close()
	
	pylab.plot(y, z, 'k')
	pylab.xlabel('y')
	pylab.ylabel('z')
	pylab.title(str(i)+' y-z')
	pylab.savefig(str(i)+'_y-z.jpg')
	pylab.close()
	
