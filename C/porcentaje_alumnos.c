#include <stdio.h>
#include <stdlib.h>
#define p printf
#define s scanf
main()
{
    system("color 70");
    float pa,pb;
    int a,b,x;
    printf("PROGRAMA 6\n");
    printf("PORCENTAJE DE ALUMNOS Y ALUMNAS\n");
    p ("\nDame el numero de alumnos: ");
    s ("%i",&a);
    p ("Dame el numero de alumnas: ");
    s ("%i",&b);
    if(a<0 || b<0)
    p ("Error\n");
    else
    {x=a+b;
    pa=(a*100)/x;
    pb=(b*100)/x;
    p ("\nEl porcentaje de alumnos es: %.2f\n",pa);
    p ("El porcentaje de alumnas es: %.2f\n\n",pb);
    }
    system ("pause");
    return 0;
}
