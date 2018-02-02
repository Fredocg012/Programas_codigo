#include <stdio.h>
#include <stdlib.h>
main()
    {system("color 5F");
     int a,b,c;
     printf("Ingresa el primer valor: ");
     scanf("%i",&a);
     printf("Ingresa el segundo valor: ");
     scanf("%i",&b);
     c=a+b;
     FILE *apuntador;
     apuntador=fopen("resultado.txt","w");
     fprintf(apuntador,"%i",c);
     fclose(apuntador);
}
