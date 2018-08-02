#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){

	float a, b, c, f1, h1, h2;
	
	printf("\n *** USO DE LA ECUACION CUADRATICA ***\n\n");
	printf(" Hola usuarios :3, Bienvenidos!!\n");
	printf("\n El dia de hoy vamos hallar las raices de una ecuacion cuadratica utilizando la formula general\n");
	printf(" teniendo en cuenta 3 datos numericos fundamentales planteados en la ecuacion y determinaremos si\n");
	printf(" es una ecuacion REAL o COMPLEJA.\n\n");
	
	printf("\n Por favor, ingresa los siguientes valores de acuerdo a la ecuacion general ax^2 + bx + c= 0\n\n");
	printf(" Ingresa el valor de 'a': ");
	scanf("%f",&a);
	printf(" Ingresa el valor de 'b': ");
	scanf("%f",&b);
	printf(" Ingresa el valor de 'c': ");
	scanf("%f",&c);

	printf("\n De acuerdo a los datos ingresados, la ecuacion cuadratica a evaluar es: (%.f)x^2 + (%.f)x + (%.f)= 0\n\n", a,b,c);

	if(a==0 || b==0 || c==0){ //Condicion para evitar inconsistencias matematicas
		
		printf(" No es posible obtener las raices de la ecuacion debido a que se puede generar una 'inconsistencia matematica'\n");
		printf(" (el valor de 'b', 'c' y en especial el de 'a' deber ser distinto de 0) \n\n Hasta pronto!! \n\n");
	
	}else{
		
		printf("\n ** PROCEDIMIENTO ** \n\n");
		

		printf("\n PASO 1: \n\n"); //Mediante teoria, se determina si la ecuacion cuadratica tiene raices reales
		printf(" * Si [ b^2 - 4ac >= 0 ], las raices de la ecuacion cuadratica son numeros reales\n");
		printf(" * Si [ b^2 - 4ac < 0 ], las raices de la ecuacion cuadratica son numeros complejos\n");
		f1 = (b*b)-(4*a*c);
		printf("\n\n Calculando (%.f)^2 - 4(%.f)(%.f) da como resultado: %.f", b,a,c,f1);
		if(f1<0){
			printf("\n\n Como [ %.f < 0 ], se puede determinar que al menos una raiz es compleja",f1);
			printf("\n\n Por lo tanto, no se pueden determinar en este programa ...");
			printf("\n\n Hasta pronto!! \n\n");
			return 0; //Como la ecuacion cuadratica tiene reices complejas se cierra el programa correctamente
		}
		printf("\n\n Como [ %.f >= 0 ], se puede determinar que las raices son numeros reales\n\n",f1);


		printf("\n PASO 2: \n\n"); //Mediante el uso de la formula general se encuentran las raices de la ecuacion cuadratica
		printf(" * Las raices de una ecuacion cuadratica se calculan con las formulas: \n\n");
		printf("      h1 = [ -b + sqrt((b^2)-4ac) ] / 2a\n");
		printf("      h2 = [ -b - sqrt((b^2)-4ac) ] / 2a\n\n Por lo tanto ambas raices son: ");
		h1=((-1*b)+sqrt((b*b)-(4*a*c)))/(2*a);
		h2=((-1*b)-sqrt((b*b)-(4*a*c)))/(2*a);
		printf("\n\n Raiz h1 = %.2f\n",h1);
		printf("\n Raiz h2 = %.2f\n\n",h2);

		
		if(h1!=h2){
			printf("\n Por lo tanto, la ecuacion cuadratica (%.f)x^2 + (%.f)x + (%.f)= 0 tiene dos raices reales\n\n", a,b,c);
		}else{ //En algunas ecuaciones cuadraticas las raices son iguales, por lo que solo se consideran 1 sola raiz
			printf("\n Por lo tanto, la ecuacion cuadratica (%.f)x^2 + (%.f)x + (%.f)= 0 tiene una raiz real\n\n", a,b,c);
		}
		printf(" LO HAS LOGRADO, BUEN TRABAJO QUERIDO USUARIO :D!!\n\n");
	}
	
	system("pause");
	return 0;
}
