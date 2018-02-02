#include <stdio.h>
#include <stdlib.h>
#include <math.h>
main()
    {
     system("color 5F");
     int i;
     float n;
     for(i=0;i<=9;i++)
         {
          n=pow(i,2);
          printf("%i\t%.0f\n",i,n);
     }
system("pause");
return 0;
}
