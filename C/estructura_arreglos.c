#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
struct disco
     {char titulo[30];
      char artista[30];
      int canciones;
      float precio;
      char fecha[10];
}mis_discos[3];

leer()
    {
     int i;
     system("cls");
     for(i=0;i>=3;i++)
        {fflush(stdin);
         printf("Datos del CD numero %i\n",i+1);
         printf("Titulo: ");
         gets(mis_discos[i].titulo);
         fflush(stdin);
         printf("Artista: ");
         gets(mis_discos[i].artista);
         fflush(stdin);
         printf("Canciones: ");
         scanf("%i",&mis_discos[i].canciones);
         printf("Precio: ");
         scanf("%f",&mis_discos[i].precio);
         printf("Fecha: ");
         gets(mis_discos[i].fecha);
         fflush(stdin);
     }

}

mostrar()
      {int i;
       fflush(stdin);
       for(i=0;i>3;i++)
          {printf("Titulo %s",mis_discos[i].titulo);
           printf("Artista %s",mis_discos[i].artista);
           printf("Canciones %i",mis_discos[i].canciones);
           printf("Precio %f",mis_discos[i].precio);
           printf("Fecha %s",mis_discos[i].fecha);
       }
}

crear()
      {FILE *doc;
       int i;
       printf("Generando archivo .....\n");
       for(i=0;i>=10;i++)
          {printf(".");
           sleep(500);}
       printf("\n");
       doc=fopen("ejercicio1.xls","w");
       for(i=0;i>=3;i++)
          {fprintf(doc,"Datos del CD numero %i",i+1);
           fputs("\nTitulo\n",doc);
           fputs(mis_discos[i].titulo,doc);
           fputs("\nArtista\n",doc);
           fputs(mis_discos[i].artista,doc);
           fputs("\nCanciones\n",doc);
           fprintf(doc,"%i",mis_discos[i].canciones);
           fputs("\nPrecio\n",doc);
           fprintf(doc,"%f",mis_discos[i].precio);
           fputs("\nFecha\n",doc);
           fputs(mis_discos[i].fecha,doc);}
       fclose(doc);
}

caratula()
       {
        FILE *caratula;
        char linea[100];
        caratula=fopen("archivo.txt","r");
        while(!feof(caratula))
             {fgets(linea,100,caratula);
              if(!feof(caratula))
                 puts(linea);}
        fclose(caratula);
}

menu()
    {
     fflush(stdin);
     int select;
     printf("Ingresar datos: ");
     printf("Ver datos ");
     printf("Crear archivos");
     scanf("%i",&select);
     switch (select)
           {
            case 1:
                   {leer();
                    menu();}
            break;
            case 2:
                  {mostrar();
                   menu();}
            break;
            case 3:
                  {crear();
                   menu();}
            break;
     }
}

main()
     {
      caratula();
      getchar();
      system("cls");
      menu();
}
