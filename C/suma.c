//Programa que suma 2 numeros dados por el usuario

#include <stdio.h>
#include <stdlib.h>
main()
    {
     system("color B0");
     float a,b,r;

     printf("SUMA DE NUMEROS\n\n");

     printf("Ingresa el valor de a: ");
     scanf("%f",&a);
     printf("Ingresa el valor de b: ");
     scanf("%f",&b);
     r=a+b;
     printf("Suma = %.2f\n",r);
     system("pause");
     return 0;
}
