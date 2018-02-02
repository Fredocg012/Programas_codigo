/*Programa que muestra los numeros del 1 al 9
  usando el ciclo While*/

#include <stdio.h>
#include <stdlib.h>
main()
    {
     printf("UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO\n");
     printf("FACULTAD DE INGENIERIA\n\n");
     system("color 5F");
     int i;
     i=1;
     while(i<10)
          {printf("%i\n",i);
           i=i+1;}
     printf("\n");
  system("pause");
  return 0;
}
