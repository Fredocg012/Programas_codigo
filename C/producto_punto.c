#include <stdio.h>
#include <stdlib.h>
#define p printf
#define s scanf
main()
{
    system("color 70");
    float a1,a2,a3,b1,b2,b3,x,x1;
    p ("PROGRAMA 3\n");
    p ("PRODUCTO PUNTO\n");
    p ("\nIngrese los 3 datos de los vectores a: ");
    s ("%f, %f, %f",&a1, &a2, &a3);
    p ("Ingrese los 3 valores de los vectores b: ");
    s ("%f, %f, %f", &b1, &b2, &b3);
    x= (((2*a1)*(5*b1))+((2*a2)*(5*b2))+((2*a3)*(5*b3)));
    x1= ((a1*b1)+(a2*b2)+(a3*b3));
    p ("\n* Para (2a x 5b) el producto punto es: %.2f\n", x);
    p ("* Para (a x b) el producto punto es: %.2f\n\n", x1);
    system("pause");
    return 0;
}
