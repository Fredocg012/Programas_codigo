//Determinar si los datos dados por el usuario representan un triángulo (isóceles,escaleno,equilatero)

#include <stdio.h>
#include <stdlib.h>
main()
    {
     int a,b,c,m;

     printf("DETERMINACION DE TRIANGULOS\n");
     printf("\n");

     printf("Ingresa el valor de a: ");
        scanf("%i",&a);
     printf("Ingresa el valor de b: ");
        scanf("%i",&b);
     printf("Ingresa el valor de c: ");
        scanf("%i",&c);
     if(a>b && a>c)
       {m=a;}
             else if(b>a && b>c)
                    {m=b;}
             else
                 {m=c;}
     if(m<(a+b+c-m))
            {if(a==b && b==c)
               {printf("Triangulo Equilatero\n");}
             else if(a==b && b!=c)
                    {printf("Triangulo isoceles\n");}
             else if(a==c && c!=b)
                    {printf("Triangulo isoceles\n");}
             else if(b==c && c!=a)
                    {printf("Triangulo isoceles\n");}
             else
                 {printf("Triangulo Escaleno\n");}
            }
     else
         {printf("No es triangulo\n");}
  system("pause");
  return 0;
}
