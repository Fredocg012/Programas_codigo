#include <stdio.h>
#include <stdlib.h>
main()
    {
     int mat[3][3];
     int i,j;
     for(i=0;i<=3-1;i++)
         for(j=0;j<=3-1;j++)
           {printf("Ingresa datos %i,%i: ",i,j);
            scanf("%i",&mat[3][3]);}
     for(i=0;i<=3-1;i++)
         printf("Valor %i = %i\n",i++,mat[3][3]);
}
