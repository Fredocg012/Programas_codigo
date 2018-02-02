#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define p printf
#define s scanf
main()
{
    system("color 70");
    float vi,vf,d,a,v,t;
    p ("PROGRAMA 8\n");
    p ("ACELERACION DE UN CUERPO\n");
    p("\nIntroduce la velocidad inicial: ");
    s("%f",&vi);
    p("Introduce la velocidad final: ");
    s("%f",&vf);
    p("Introduce la distancia: ");
    s("%f",&d);
    v=(vf-vi)/2;
    t=d/v;
    a=v/(t*t);
    p("\nLa aceleracion es de %.2f\n\n",a);
    system("pause");
    return 0;
}
