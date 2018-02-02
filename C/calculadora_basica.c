//Calculadora Basica (suma,resta,division,multiplicacion)

#include <stdio.h>
#include <stdlib.h>
//Creador: Jesus RM
float a,b,r;
main()
    {
     printf("UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO\n");
     printf("FACULTAD DE INGENIERIA\n");
     printf("\nCALCULADORA BASICA\n");
     printf("\n****  MENU  ****\n");
     printf("\n* Suma (Teclea 1)\n");
     printf("* Resta (Teclea 2)\n");
     printf("* Multiplicacion (Teclea 3)\n");
     printf("* Division (Teclea 4)\n");

     int n;
     printf("\nElige, de acuerdo al MENU, la operacion a realizar: ");
     scanf("%i",&n);

     switch(n)
             {
              case 1:
                     printf("\nIngresa el valor de a: ");
                            scanf("%f",&a);
                     printf("Ingresa el valor de b: ");
                            scanf("%f",&b);
                     r=a+b;
                     printf("\nResultado Suma = %.2f\n\n",r);
                  break;

              case 2:
                     printf("\n***  SUBMENU  ***\n");
                     printf("\n* Restar a-b (Teclea 1)\n");
                     printf("* Restar b-a (Teclea 2)\n");
                     printf("\nElige, de acuerdo al SUBMENU, el tipo de resta: ");
                     scanf("%i",&n);
                     switch(n)
                              {
                               case 1:
                                      printf("\nIngresa el valor de a: ");
                                      scanf("%f",&a);
                                      printf("Ingresa el valor de b: ");
                                      scanf("%f",&b);
                                       {r=a-b;
                                       printf("\nResultado Resta = %.2f\n\n",r);}
                                   break;

                               case 2:
                                      printf("\nIngresa el valor de a: ");
                                      scanf("%f",&a);
                                      printf("Ingresa el valor de b: ");
                                      scanf("%f",&b);
                                      {r=b-a;
                                       printf("\nResultado Resta = %.2f\n\n",r);}
                                    break;

                               default:
                                       printf("\nError\n\n");
                                }
                  break;

              case 3:
                     printf("\nIngresa el valor de a: ");
                           scanf("%f",&a);
                     printf("Ingresa el valor de b: ");
                           scanf("%f",&b);
                     r=a*b;
                     printf("\nResultado Multiplicacion = %.2f\n\n",r);
                   break;

              case 4:
                     printf("\n***  SUBMENU  ***\n");
                     printf("\n* Dividir a/b (Teclea 1)\n");
                     printf("* Dividir b/a (Teclea 2)\n");
                     printf("\nElige, de acuerdo al SUBMENU, el tipo de division: ");
                     scanf("%i",&n);
                     switch(n)
                              {
                               case 1:
                                      printf("\nIngresa el valor de a: ");
                                      scanf("%f",&a);
                                      printf("Ingresa el valor de b: ");
                                      scanf("%f",&b);
                                      if (a!=0 && b!=0)
                                              {r=a/b;
                                               printf("\nResultado Division = %.2f\n\n",r);}
                                      else
                                          printf("\nError\n\n");
                                   break;

                               case 2:
                                      printf("\nIngresa el valor de a: ");
                                      scanf("%f",&a);
                                      printf("Ingresa el valor de b: ");
                                      scanf("%f",&b);
                                      if (a!=0 && b!=0)
                                              {r=b/a;
                                               printf("\nResultado Division = %.2f\n\n",r);}
                                      else
                                          printf("\nError\n\n");
                                    break;

                               default:
                                       printf("\nError\n\n");
                                }
                break;

                default:
                       printf("\nError\n\n");
              }
    return 0;
}
