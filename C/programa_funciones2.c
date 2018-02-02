#include <stdio.h>
#include <stdlib.h>
saludar()
       {
        printf("Hola a todos!!\n");
          }
despedirse()
           {
             printf("Adios!!\n");
           }
main()
    {
     system("color 5F");
     char nombre[50];
     saludar();
     printf("Ingresa tu nombre: ");
     gets(nombre);
     despedirse();
system("pause");
return 0;
     }
