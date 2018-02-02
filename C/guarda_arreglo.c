#include <stdio.h>
#include <stdlib.h>
GuardaArreglo(float vect[],int tam)
              {int i;
               for(i=0;i<tam;i++)
                  {printf("\nArreglo[%i] =",i);
                   scanf("%f",&vect[i]);}
              ImprimeArreglo(vect,tam);}

ImprimeArreglo(float array[],int longitud)
              {int i;
               for(i=0;i<longitud;i++)
                  {printf("[%i]->%.0f\n",i,array[i]);}}

suma(float a[],float b[], int dime)
    {int i;
     for(i=0;i<dime;i++)
        {a[i]=a[i]+b[i];
        printf("Resultado -> %.0f\n",a[i]);}
    }

main()
     {
      system("color 5F");
      int dim;
      printf("Ingresa la dimensiones: ");
      scanf("%i",&dim);
      float arreglo[dim];
      float arregloB[dim];
      if(dim>=100)
               {printf("No puedo");}
      else
          {GuardaArreglo(arreglo,dim);
           GuardaArreglo(arregloB,dim);
           suma(arreglo,arregloB,dim);}
system("pause");
return 0;
}

