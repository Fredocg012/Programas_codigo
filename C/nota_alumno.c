#include <stdio.h>
#include <stdlib.h>

int i;

void alu_nota(char nombre[4][50], int nota[4]){
	for(i=0;i<4;++i)
	{
		printf("Ingrese el nombre del alumno %i: ", i+1);
		gets(nombre[i]);
		printf("Ingrese la nota del alumno %i: ",i+1);
		scanf("%i", & nota[i]);
		fflush(stdin);
	}
}

void imprimir(char nombre[4][50], int nota[4]){
	int muybueno=0;
	for(i=0;i<4;++i)
	{
		printf("** ALUMNO %i **\n",i+1);
		printf("Nombre: %s\n", nombre[i]);
		printf("Nota: %i\n", nota[i]);
		if(nota[i]>=8)
		{
			printf("Condicion: Muy bueno\n\n");
			muybueno=muybueno+1;
		}
		else if(nota[i]>=4 && nota[i]<=7)
		{
			printf("Condicion: Bueno\n\n");
		}
		else
		{
			printf("Condicion: Malo\n\n");
		}
	}
	printf("Alumnos con condicion Muy buena: %i\n\n",muybueno);
}

int main(){
	char nombre[4][50];
	int nota[4];
	printf("\n");
	alu_nota(nombre,nota);
	printf("\n");
	imprimir(nombre,nota);
	return 0;
}