#include <stdio.h>
#include <stdlib.h>
cuadrados()
       {int i;
        float n;
        for(i=0;i<=9;i++)
           {
            n=pow(i,2);
            printf("%i\t%.0f\n",i,n);}}
suma()
           {int a,b,c;
            printf("Ingresa el primer numero: ");
            scanf("%i",&a);
            printf("Ingresa el segundo numero: ");
            scanf("%i",&b);
            c=a+b;
            printf("Resultado = %i\n\n",c);}

int resta(int p, int q)
       {int res;
        res=p-q;}
main()
     {
      system("color 5F");
      int n;
      printf("*** MENU ***\n");
      printf("* Cuadrados de numeros N (1)\n");
      printf("* Suma de numeros        (2)\n");
      printf("\nDe acuardo al menu, elige una opcion: ");
      scanf("%i",&n);
      switch(n)
              {case 1:
                      printf("\n");
                      cuadrados();
                      printf("\n");
                   break;
               case 2:
                      printf("\n");
                      suma();
                   break;
               case 3:
                      {int m,n,resultado;
                      printf("\nIngresa el primer numero: ");
                      scanf("%i",&m);
                      printf("Ingresa el segundo numero: ");
                      scanf("%i",&n);
                      resultado=resta(m,n);
                      printf("Resultado = %i\n\n",resultado);}
                    break;
               default:
                       printf("\n");
                       printf("Error!\n\n");}
system("pause");
return 0;
     }
