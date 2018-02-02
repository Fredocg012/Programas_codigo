#include <stdio.h>
#include <stdlib.h>
#define m 1000
#define s 3600
       main()
           {
            system("color 70");
            float a,r;
            printf("PROGRAMA 5\n");
            printf("CONVETIDOR DE KM/H A M/S\n");
            printf("\nIngresa la velocidad en Km/h: ");
            scanf("%f",&a);
            if(a>0)
               {r=(a*m)/s;
               printf("\nLa velocidad en m/s = %.2f\n\n",r);}
            else
            {printf("\nError!\n\n");}
        system("pause");
        return 0;
}
