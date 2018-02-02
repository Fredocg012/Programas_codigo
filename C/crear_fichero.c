#include <stdio.h>
#include <stdlib.h>
main()
    {
     FILE *fp1,*fp2;
     fp1=fopen("archivo.txt","r");
     if(fp1==NULL)
        {printf("Error al abrir el archivo para leer\n");}
     fp2=fopen("Copia.txt","w");
     if(fp2=NULL)
        {printf("Error al abrir el archivo copia.txt\n");}
     fclose(fp1);
     fclose(fp2);
}
