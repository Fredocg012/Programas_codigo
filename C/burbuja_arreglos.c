#include <stdio.h>

int main(){
	
	int arreglo[10]={4,2,5,1,3,-6,0,7,9,-2}; //Declaración de un arreglo con 10 numeros
	int i, j, aux; //Declaración de variables de control 'i' y 'j', añadiendo una variable auxiliar 'aux'
	
	for(i=0; i<10; ++i) //Recorrido del arreglo
	{
		for(j=0; j<10; ++j)  
		{
			if(arreglo[j]>arreglo[j+1]) //Se analizan los valores almacenados en el arreglo de dos en dos
			{
				aux = arreglo[j]; //Guarda el valor almacenado en el arreglo[j] en la variable 'aux'
				arreglo[j] = arreglo[j+1]; //Intercambio de valores
				arreglo[j+1] = aux;
			}
		}
	}
	
	for(i=0; i<10; ++i) //Impresión del resultado en pantalla
	{
		printf("%i ", arreglo[i]);
	}

	return 0;
}
