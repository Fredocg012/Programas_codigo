#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int opc,m,n,resultado;

menu()
     {printf("***** CALCULADORA BASICA *****\n");
      printf("\n    *** MENU ***\n");
      printf("* Suma           (1) *\n");
      printf("* Resta          (2) *\n");
      printf("* Multiplicacion (3) *\n");
      printf("* Division       (4) *\n");}

dame_datos()
           {printf("\nIngresa el primer numero: ");
            scanf("%i",&m);
            printf("Ingresa el segundo numero: ");
            scanf("%i",&n);}

dame_datos2()
            {printf("\nIngresa el numero que vas a dividir: ");
            scanf("%f",&a);
            printf("Ingresa el numero al que vas a dividir: ");
            scanf("%f",&b);}

int suma(int p, int q)
                     {int res;
                      res=p+q;}

int resta(int p, int q)
                      {int res;
                       res=p-q;}

int multiplicacion(int p, int q)
                      {int res;
                       res=p*q;}

division(int p, int q)
                      {float res;
                       res=p/q;}

main()
     {system("color 5F");
      menu();
      printf("\nDe acuardo al menu, elige una opcion: ");
      scanf("%i",&opc);

   switch(opc)
           {case 1:
                   {dame_datos();
                    resultado=suma(m,n);
                    printf("Resultado = %i\n\n",resultado);}
                 break;
            case 2:
                   {dame_datos();
                    resultado=resta(m,n);
                    printf("Resultado = %i\n\n",resultado);}
                 break;
            case 3:
                   {dame_datos();
                    resultado=multiplicacion(m,n);
                    printf("Resultado = %i\n\n",resultado);}
                 break;
            case 4:
                   {float a,b;
                    dame_datos2();
                    resultado=division(a,b);
                    printf("Resultado = %f\n\n",resultado);}
                 break;
            default:
                    printf("\nError!\n\n");}
system("pause");
return 0;
}
