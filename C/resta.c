//Programa que resta 2 numeros dados por el usuario

#include <stdio.h>
#include <stdlib.h>
main()
    {
     system("color B0");
     int opc;
     float a,b,r;

     printf("RESTA DE NUMEROS\n\n");

     printf("Ingresa el valor de a: ");
     scanf("%f",&a);
     printf("Ingresa el valor de b: ");
     scanf("%f",&b);
     printf("Quieres a-b (escribe 1) o b-a (escribe 2): ");
     scanf("%i",&opc);
           if(opc==1)
              {r=a-b;
              printf("Resta= %.2f\n",r);}
           else if(opc==2)
              {r=b-a;
              printf("Resta= %.2f\n",r);}
           else
               printf("Error\n");
    system("pause");
    return 0;
}
