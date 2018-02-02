#include <stdio.h>
#include <stdlib.h>
main()
    {
     printf(" UNIVERSIDAD NACIONAL AUT%cNOMA DE M%cXICO\n",224,144);
     printf(" FACULTAD DE INGENIER%cA\n\n",214);
     system("color 5F");
     int n,i;
     for(i=0;i<=10;i++)
        {printf(" Tabla del %d\n",i);
         for(n=1;n<=10;n++)
         printf(" %dx%d=%d\n",i,n,i*n);
         printf("\n");}
  system("pause");
  return 0;
}
