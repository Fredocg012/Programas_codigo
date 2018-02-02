/*
  Programa        :   producto_matriz.c
  Alumno          :   Rosas Mart�nez Jes�s Adri�n
  Fecha de entrega:   18 de agosto de 2017
*/

#include<stdio.h>
#include<stdlib.h>

/*Programa que solicita al usuario las dimensiones de 2 matrices.
  El programa ser� capaz de indicar al usuario si las matrices se pueden multiplicar, si se cumple
  la condici�n mostrar� la matriz resultante; en caso contrario finalizar� el programa.
*/

void PrimeraMatriz();
void SegundaMatriz();
void Datos_Producto();

int renglonA, columnaA, renglonB, columnaB; //Variables globales para guardar dimensiones de la matriz
int i, j, k; //Variables de control 

int main(){
	printf("\n * MULTIPLICACION DE MATRICES *\n");
	PrimeraMatriz(); //Funci�n que pide las dimensiones de la primera matriz
	SegundaMatriz(); //Funci�n que pide las dimensiones de la segunda matriz
	if(columnaA!=renglonB) //Verificar si se puede hacer la mutiplicaci�n matricial
    {
		printf("\nNo es posible multiplicar ambas matrices\n");
	}
	else
	{
	    printf("\n** Valores\n\n");
	    Datos_Producto(); //Funci�n que pide los datos de las matrices, calcula y muestra su multiplicaci�n
	    printf("\n");
	}

	return 0;
}

void PrimeraMatriz(){ //Dimensiones de la primera matriz
    printf("\n** Dimension: Primera Matriz\n");
	printf("\nIngresa el numero de renglones: ");
	scanf("%d", &renglonA);
	printf("Ingresa el numero de columnas: ");
	scanf("%d", &columnaA);
}

void SegundaMatriz(){ //Dimensiones de la segunda matriz
    printf("\n** Dimension: Segunda Matriz\n");
	printf("\nIngresa el numero de renglones: ");
	scanf("%d", &renglonB);
	printf("Ingresa el numero de columnas: ");
	scanf("%d", &columnaB);
}

void Datos_Producto(){ //Guardar valores de las matrices, y mostrar en pantalla el resultado al mutiplicarlas
    int A[renglonA][columnaA], B[renglonB][columnaB], AB[renglonA][columnaB]; //Declaraci�n de arreglos
    for(i=0; i<renglonA; ++i) //Pedir los valores de la primera matriz segun su posici�n en ella
    {
        for(j=0; j<columnaA; ++j)
        {
           printf("Ingresa el valor (%i,%i) de la Primera Matriz: ", i+1, j+1);
           scanf("%d",&A[i][j]);
        }
    }

    printf("\n\n");

    for(i=0; i<renglonB; ++i) //Pedir los valores de la segunda matriz seg�n su posici�n en ella
    {
        for(j=0; j<columnaB; ++j)
        {
           printf("Ingresa el valor (%i,%i) de la Segunda Matriz: ", i+1, j+1);
           scanf("%d",&B[i][j]);
        }
    }

    for(i=0; i<renglonA; ++i) //Multplicaci�n de las matrices
    {
        for(j=0; j<columnaB; ++j)
        {
            AB[i][j]=0;
            for(k=0; k<columnaA; ++k)
            {
                AB[i][j]=AB[i][j]+(A[i][k]*B[k][j]);
            }
        }
    }

    printf("\n** La multiplicacion de las matrices (A*B) es: ");
    printf("\n\n\t\t\t Matriz A*B\n");
    for(i=0;i<renglonA;++i) //Imprimir en pantalla en forma de matriz el resultado al multiplicar ambas matrices
    {
        printf("\n\t\t");
        for(j=0;j<columnaB;++j)
        {
            printf("%6d", AB[i][j]);
        }
    }
}

