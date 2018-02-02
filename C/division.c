//Programa que divide 2 numeros dados por el usuario

#include <stdio.h>
#include <stdlib.h>
main()
    {
     system("color F0");
     int opc;
     float a,b,r;

     printf("DIVISION DE NUMEROS\n\n");

     printf("Ingresa el valor de a: ");
     scanf("%f",&a);
     printf("Ingresa el valor de b: ");
     scanf("%f",&b);
     if (b!=0 && a!=0)
        {printf("Quieres a/b (escribe 1) o b/a (escribe 2): ");
         scanf("%i",&opc);
              if(opc==1)
                 {r=a/b;
                 printf("Division = %.2f\n",r);}
              else if(opc==2)
                 {r=b/a;
                 printf("Division = %.2f\n",r);}
              else
                 printf("Error\n");}
     else
         printf("Error");
    system("pause");
    return 0;
}
