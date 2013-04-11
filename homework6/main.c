#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "derivative.h"
#include "runge-kutta.h"

int main ()
{
	FILE *export;
	export = fopen("answer.dat", "w");
	double h;
	int n_points;
	h = 0.01;
	n_points = (int) ((30.0+h)/h);
	
	double *t;
	double *x;
	double *y;
	double *z;
	
	double sigma;
	double beta;
	double rho;
	
	sigma = 10.0;
	beta = 8.0/3.0;
	rho = 28.0;
	
	x = malloc(n_points*sizeof(double));
	y = malloc(n_points*sizeof(double));
	z = malloc(n_points*sizeof(double));
	t = malloc(n_points*sizeof(double));

	x[0] = 5.0;
	y[0] = 8.0;
	z[0] = 1.0;
	t[0] = 0.0;
	fprintf(export,"%f %f %f %f \n", t[0],x[0],y[0],z[0]);
	
	int i;
	
	for (i = 1; i < n_points; i ++)
	{
		rungekutta_step(i,x,y,z,t,sigma,beta,rho,h);
		fprintf(export,"%f %f %f %f \n", t[i],x[i],y[i],z[i]);
	}
	
	return 0;
}
