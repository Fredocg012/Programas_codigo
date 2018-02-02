/*
  Programa        :   programa1.c
  Alumno          :   Rosas Martínez Jesús Adrián
  Fecha de entrega:   22 de agosto de 2017
*/

#include<stdio.h>

/*
  Este programa crea un apuntador de tipo caracter
*/

int main(){
	
	char *ap, c;
	c = 'x';
	ap = &c;

	//Imprime el caracter de la localidad a la que apunta
	printf("Caracter: %c\n", *ap);
	//Imprime el codigo ASCII de la localidad a la que apunta
	printf("Codigo ASCII: %d\n", *ap);
	//Imprime la direccion de memoria de la localidad a la que apunta
	printf("Direccion de memoria: %d\n",(unsigned char)ap);

	return 0;
}