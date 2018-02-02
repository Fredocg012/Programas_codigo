#include <stdio.h>
#include <stdlib.h>
#include <math.h>
main()
    {
     int n;
     system("color 5F");
     printf(" Multiplos de 2 y 3\n\n");
     n=0;
     n=n+1;
     do
       {
        if(n%2==0 || n%3==0)
        printf(" %i\n",n);
        n=n+1;
       }
     while(n>1 && n<=100);
     printf("\n");
 system("pause");
 return 0;
}
