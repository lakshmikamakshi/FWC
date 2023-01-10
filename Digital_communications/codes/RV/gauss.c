#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"


int  main(void) //main function begins
{
 
//Gaussian random numbers
gaussian("gauss.dat", 1000000);

//Mean and variance of Gaussian 
printf("Mean: %lf\n",mean("gauss.dat"));
printf("Variance: %lf\n",variance("gauss.dat"));
return 0;
}
