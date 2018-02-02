#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define pi 3.1416
#define F 42
main()
    {
     system("color 70");
     float area,presion;

     printf("PROGRAMA 4\n");
     printf("DETERMINACION DE LA PRESION DE UN FLUIDO EN UNA JERINGA\n\n");

     printf("\n***  A =2(pi)r^2  ***\n");
           area=2*pi*(1.1e-2)*(1.1e-2);
     printf("* Area del piston de la jeringa = %.5f [m^2]\n",area);
     printf("\n***  P = F/A  ***\n");
           presion= F/area;
     printf("* Presion del fluido = %.2f [N/m^2]\n\n",presion);

  system("pause");
  return 0;
}
