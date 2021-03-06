#include <stdio.h>
#include <math.h>
#include "derivative.h"

int rungekutta_step(int i, double *x,double *y,double *z,double *t,double sigma, double beta, double rho, double h)
{
	double kx1 = x_prime(x[i-1],y[i-1],z[i-1],sigma,beta,rho);
	double ky1 = y_prime(x[i-1],y[i-1],z[i-1],sigma,beta,rho);
	double kz1 = z_prime(x[i-1],y[i-1],z[i-1],sigma,beta,rho);
    
 	// first step
	double t1 = t[i-1] + (h/2.0);
	double x1 = x[i-1] + (h/2.0) * kx1;
	double y1 = y[i-1] + (h/2.0) * ky1;
	double z1 = z[i-1] + (h/2.0) * kz1;
	
	double kx2 = x_prime(x1, y1, z1, sigma, beta, rho);
	double ky2 = y_prime(x1, y1, z1, sigma, beta, rho);
	double kz2 = z_prime(x1, y1, z1, sigma, beta, rho);
   
	// second step
	double t2 = t[i-1] + (h/2.0);
	double x2 = x[i-1] + (h/2.0) * kx2;
	double y2 = y[i-1] + (h/2.0) * ky2;
	double z2 = z[i-1] + (h/2.0) * kz2;
	
	double kx3 = x_prime(x2, y2, z2, sigma, beta, rho);
	double ky3 = y_prime(x2, y2, z2, sigma, beta, rho);
	double kz3 = z_prime(x2, y2, z2, sigma, beta, rho);
 		      
	// third step
 	double t3 = t[i-1] + h;
  	double x3 = x[i-1] + h * kx3;
  	double y3 = y[i-1] + h * ky3;
  	double z3 = z[i-1] + h * kz3;
  	
  	double kx4 = x_prime(x3, y3, z3, sigma, beta, rho);
  	double ky4 = y_prime(x3, y3, z3, sigma, beta, rho);
  	double kz4 = z_prime(x3, y3, z3, sigma, beta, rho);
  	
  	// fourth step
 	double average_kx = (1.0/6.0)*(kx1 + 2.0*kx2 + 2.0*kx3 + kx4);
 	double average_ky = (1.0/6.0)*(ky1 + 2.0*ky2 + 2.0*ky3 + ky4);
 	double average_kz = (1.0/6.0)*(kz1 + 2.0*kz2 + 2.0*kz3 + kz4);
    
  	t[i] = t[i-1] + h;
   	x[i] = x[i-1] + h * average_kx;
   	y[i] = y[i-1] + h * average_ky;
   	z[i] = z[i-1] + h * average_kz;
}
