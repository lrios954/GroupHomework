#include <stdio.h>
#include <math.h>

double x_prime(double x,double y,double z,double sigma, double beta, double rho)
{	
	return sigma*(y-x);
}

double y_prime(double x,double y,double z,double sigma, double beta, double rho)
{	
	return x*(rho-z)-y;
}
   
double z_prime(double x,double y,double z,double sigma, double beta, double rho)
{	
	return x*y-beta*z;
}
     
    
