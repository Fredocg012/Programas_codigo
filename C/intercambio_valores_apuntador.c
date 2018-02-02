/*
  Programa        :   programa3.c
  Alumno          :   Rosas Martínez Jesús Adrián
  Fecha de entrega:   22 de agosto de 2017
*/

#include<stdio.h>

/*Este programa intercambia los valores guardados de
  dos variables usando apuntadores
*/

void swap(int *x, int *y);

int main(){
	int a=10, b=5;
	printf("* Primeros valores *\n");
	printf("a = %i\nb = %i\n", a,b );
	swap(&a, &b);
	printf("\n* Valores Intercambiados *\n");
	printf("a = %i\nb = %i\n", a,b );
	
	return 0;
}

void swap(int *x, int *y){
	int temp =*x;
	*x = *y;
	*y = temp;
}