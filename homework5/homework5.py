import os
import numpy
from scipy.fftpack import fft, fftfreq, ifft
import sys
import pylab
import scipy

# Carga los datos

data = numpy.loadtxt(open(os.path.expanduser('hw5_data/monthrg.dat'), 'r'))

# Grafica el numero de manchas solares en funcion del tiempo

sunspots = []
time = []

for line in data:
	if (line[0] >= 1800):
		sunspots.append(line[3])
		time.append(line[0] + line[1]/12.0)	

pylab.plot(time, sunspots, '.')
pylab.xlabel('Time (Years)')
pylab.ylabel('Average Number of Sunspots')
pylab.savefig('sunspots')
pylab.grid(True)
pylab.show()

# Calcula la transformada de Fourier y el espectro de potencias

fourier = fft(sunspots) / len(sunspots)
freq = fftfreq(len(time), 1.0/12.0)
power = numpy.abs(fourier) ** 2

# Grafica el  espectro de potencias en funcion de la frecuencia

pylab.plot(freq, power, '.')
pylab.xlabel('Frequencies (1/Years)')
pylab.ylabel('Power')
pylab.savefig('power')
pylab.grid(True)
pylab.show()

# Filtra el espectro a periodos entre 1 y 20 anios

sub_pow = []
periods = []

for i in range(len(freq)):
	
	if (freq[i] != 0.0):
	
		periodo  = 1/freq[i]
	
		if (periodo >= 1.0 and periodo <= 20.0):
	
			periods.append(periodo)
			sub_pow.append(power[i])
			
			
# Grafica el  espectro de potencias en funcion del tiempo
		
pylab.plot(periods, sub_pow, '.')
pylab.xlabel('Period (Years)')
pylab.ylabel('Power')
pylab.savefig('power_between_1_and_20')
pylab.grid(True)
pylab.show()

# Filtramos las amplitudes

new_four = fourier * len(sunspots)

for i in range(len(freq)):
	
	if (freq[i] >= 1.0/20.0):
	
		new_four[i] = 0.0
	if (freq[i] <= -1.0/20.0):
	
		new_four[i] = 0.0

new_sunspots = ifft(new_four)

pylab.plot(time, numpy.abs(new_sunspots), '.')
pylab.xlabel('Time (Years)')
pylab.ylabel('Average Number of Sunspots')
pylab.savefig('new_sunspots')
pylab.grid(True)
pylab.show()
		







