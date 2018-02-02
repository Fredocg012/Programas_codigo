/*Programa que muestra el dia de la semana
conforme a el numero que escriba el usuario*/

#include <stdio.h>
#include <stdlib.h>
   main()
       {
        system("color B0");
        int n;
        printf("DIAS DE LA SEMANA\n\n");

        printf("Ingresa un numero del 1 al 7: ");
        scanf("%i",&n);
        switch(n)
               {
                case 1:
                       printf("Domingo\n");
                    break;
                case 2:
                       printf("Lunes\n");
                    break;
                case 3:
                       printf("Martes\n");
                    break;
                case 4:
                       printf("Miercoles\n");
                    break;
                case 5:
                       printf("Jueves\n");
                    break;
                case 6:
                       printf("Viernes\n");
                    break;
                case 7:
                       printf("Sabado\n");
                    break;
        default:
                printf("Error, escribir numeros del 1 al 7\n");
                }
        system("pause");
        return 0;
}
