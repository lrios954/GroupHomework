a.out: main.o dsolve.o derivative.o runge-kutta.o
	cc -lm main.o dsolve.o derivative.o runge-kutta.o

main.o: main.c
	cc -c main.c

dsolve.o: dsolve.c
	cc -c dsolve.c

derivative.o: derivative.c
	cc -c derivative.c

runge-kutta.o: runge-kutta.c
	cc -c runge-kutta.c

all: a.out

clean: 
	rm -f *.o

