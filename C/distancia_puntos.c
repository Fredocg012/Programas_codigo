#include <stdio.h>
#include <stdlib.h>
main()
{
    system("color 70");
    float a,b,a1,b1,x;
    printf("PROGRAMA 7\n");
    printf("DISTANCIA ENTRE DOS PUNTOS\n");
    printf("\nDame el valor el primer punto: ");
    scanf("%f,%f",&a,&b);
    printf("Dame el valor del segundo punto: ");
    scanf("%f,%f",&a1,&b1);
    x=sqrt((a1-a)*(a1-a))+((b1-b)*(b1-b));
    printf("\nLa distancia es de: %.2f\n\n",x);
    system ("pause");
    return 0;
}
