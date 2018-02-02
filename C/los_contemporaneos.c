#include <stdio.h>
#include <stdlib.h>
main()
    {
     int Miguel,Omar,Elizabeth;

       printf("LOS CONTEMPORANEOS\n");
       printf("\n");

         printf("Ingresa la edad de Miguel: ");
            scanf("%i",&Miguel);
         printf("Ingresa la edad de Omar: ");
            scanf("%i",&Omar);
         printf("Ingresa la edad de Elizabeth: ");
            scanf("%i",&Elizabeth);
                  if(Miguel==Omar && Omar==Elizabeth)
                    {printf("Miguel, Omar y Elizabeth son contemporaneos\n");}
                  else if(Elizabeth==Omar)
                         {printf("Elizabeth y Omar son contemporaneos\n");}
                  else if(Elizabeth==Miguel)
                         {printf("Elizabeth y Miguel son contemporaneos\n");}
                  else if(Miguel==Omar)
                         {printf("Miguel y Omar son contemporaneos\n");}
                  else
                      {printf("Nadie es contemporaneo\n");}
     system("pause");
     return 0;
     }
