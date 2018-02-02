//Programa que multiplica 2 numeros dados por el usuario

#include <stdio.h>
#include <stdlib.h>
main()
    {
     system("color B5");
     float a,b,r;

     printf("MULTIPLICACION DE NUMEROS\n\n");

     printf("Ingresa el valor de a: ");
     scanf("%f",&a);
     printf("Ingresa el valor de b: ");
     scanf("%f",&b);
     r=a*b;
     printf("Multiplicacion = %.2f\n",r);
     system("pause");
     return 0;
}
