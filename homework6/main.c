#include <stdio.h>
#include <stdlib.h>
#include "dsolve.h"


int main ()
{	
	int i;
	srand48 (getpid());
	 
	for (i = 0; i < 10; i ++)
	{  
		double x = drand48()*20.0 - 10.0 , y = drand48()*20.0 - 10.0 , z = drand48()*20.0 - 10.0;
		printf(" Resolviendo para las condiciones iniciales: %f, %f, %f. \n",x,y,z);
		dsolve(i,x,y,z);
	}
	return 0;
}

