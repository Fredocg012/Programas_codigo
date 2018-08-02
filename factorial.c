#include <stdio.h> //libreria de entra y salida necesaria para el funcionamiento del programa
#include <stdlib.h> //libreria para llamar funciones del sistema (system)

int main(){

	short num1,cont; //Variables de tipo short para guardar pequenas cantidades de datos
	long int aux, result; //Variables de tipo long para guardar grandes cantidades de datos
	char opc; //Variable para guardar letras o caracteress

	do{
		system("cls"); //limpia la pantalla o simbolo del sistema cmd

		printf("\n *** Factorial de un numero ***\n");
		printf("\n Bienvenido:\n\n A continuacion ingresa un numero entero entre (0-15): ");
		scanf("%hi",&num1); //Se guarda el dato ingresado en la variable num1
		
		if(!(num1>=0 && num1<16)){ //Se verifica si el numero ingresado esta dentro del rango permitido
			printf("\n El numero ingresado esta fuera del rango requerido\n");
		}else if(num1==0){
			printf("\n El factorial del numero 0 es: 1\n\n"); //El factorial de 0 es 1 (concepto)
		}else{
			result=num1;
			printf("\n Proceso: \n\n");
			for(cont=num1;cont>1;cont--){
				aux=result; //Se guarda el valor obtenido en cada iteracion o vuelta del ciclo
				result*=(cont-1);
				printf(" %li x %i = %li\n",aux,cont-1,result); //Se imprime en pantalla el proceso
			}
			printf("\n El factorial del numero %hi es: %li\n\n",num1,result); //resultado
		}

		do{
			printf("\n Volver a repetir el programa? (S/N): ");
			scanf("%s",&opc);
			if(opc!='S' && opc!='s' && opc!='N' && opc!='n'){ //Se verifica si el usuario ingreso "s" o "n"
				printf(" Opcion no valida ...\n");
			}else{
				break; //Se sale del ciclo si el usuario tecleo alguna opcion "s" o "n"
			}
		}while("true"); //true es para que se haga un ciclo infinito que solo un break puede romper
	
	}while(opc=='s' || opc=='S'); //Si llega a esta linea significa que tecleo "s" o "n". Si es "s" se ejecuta de nuevo, sino, se cierra

	printf("\n Hasta pronto!\n\n");

	system("pause"); //Congelar pantalla para que no se cierre al instante el programa
	return 0; //indica que el programa a terminado y se libera la memoria
}
