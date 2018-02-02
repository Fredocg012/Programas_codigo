#include <stdio.h>
#include <stdlib.h>
main()
     {
	  system("color 70");
	  char A,B,C;
      printf("PROGRAMA 1\n");
      printf("INTERCAMBIO DE VALORES\n");
	  printf("\nIngresa el valor de A: ");
      scanf("%c%c",&A);
      printf("Ingresa el valor de B: ");
      scanf("%c",&B);
      C=A;
      A=B;
      B=C;
	  printf("\nEl valor de A ahora es: %c\n",A);
	  printf("El valor de B ahora es: %c\n\n",B);
	system("pause");
	return 0;
}
