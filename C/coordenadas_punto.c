#include <stdio.h>

struct punto
{
	int x;
	int y;
};

struct punto p(){
	struct punto pun;
	printf("Ingrese la coordenada x: ");
	scanf("%i", & pun.x);
	printf("Ingrese la coordenada y: ");
	scanf("%i", & pun.y);
	return pun;
}

void imprimir(struct punto pun){
	if(pun.x>0 && pun.y>0)
	{
		printf("El punto (%i,%i) se encuentra en el primer cuadrante\n",pun.x,pun.y);
	}
	else if(pun.x<0 && pun.y>0)
	{
		printf("El punto (%i,%i) se encuentra en el segundo cuadrante\n",pun.x,pun.y);
	}
	else if(pun.x<0 && pun.y<0)
	{
		printf("El punto (%i,%i) se encuentra en el tercer cuadrante\n",pun.x,pun.y);
	}
	else if(pun.x>0 && pun.y<0)
	{
		printf("El punto (%i,%i) se encuentra en el cuarto cuadrante\n",pun.x,pun.y);
	}
	else if(pun.x==0 && pun.y==0)
	{
		printf("El punto (%i,%i) se encuentra en el origen\n",pun.x,pun.y);
	}
	else
	{
		printf("El punto (%i,%i) se encuentra sobre un eje\n",pun.x,pun.y);
	}
}

int main(){
	struct punto p1,p2,p3;
	printf("\n");
	p1=p();
	p2=p();
	p3=p();
	imprimir(p1);
	imprimir(p2);
	imprimir(p3);
	printf("\n");
	return 0;
}