#include <stdio.h>
#include <stdlib.h>
#define p printf
#define s scanf
main()
{
    system("color 70");
    char n[29];
    float su,sn,is,af,re;
    p ("PROGRAMA 2\n");
    p ("SUELDO NETO\n");
    p ("\nIngresa tu nombre: ");
    s ("%s",&n);
    p ("Ingresa tu sueldo: ");
    s ("%f",&su);
    is=(su*.05);
    af=(su*.07);
    re=(su*.1);
    sn=(su-(is+af+re));
    p ("\n%s",n);
    p (", tu sueldo neto es de: %.2f\n\n",sn);
    system ("pause");
    return 0;
}
