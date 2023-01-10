#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

void natural(char *str , int len)
{
	int i,j;
	double temp;
	FILE *fp;

	fp = fopen(str,"w");
	//Generate numbers
	for (i=0;i<len;i++)
	{
		temp =(double)rand()/RAND_MAX;
		//printf("%d",U);
		//double U = 23;
		temp = -2*log(1-temp);
	//	printf("%lf",temp);
                fprintf(fp,"%lf\n",temp);
	}
	fclose(fp);
}
int  main(void) //main function begins
{
 
//Uniform random numbers
//uniform("uni.dat", 1000000);

//Gaussian random numbers
//gaussian("gau.dat", 1000000);
//natural("nat.dat" , 1000000);
triangle("tri.dat" ,  1000000);
//Mean of uniform
//printf("%lf",log(4));
printf("%lf",mean("tri.dat"));
printf("%lf",variance("tri.dat"));
return 0;
}


