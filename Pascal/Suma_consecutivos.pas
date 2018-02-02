{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 30 de Marzo de 2016
 Asunto:Programa que realiza la suma de los numeros consecutivos a N, utilizando procedimientos y funciones
}
Program Suma_consecutivos;
Uses crt;
Var
   N:integer;  //Variables globales
   Procedure Bienvenida;
   Begin
        Writeln('**SUMA DE NUMEROS**');
   End;
   Procedure Lectura;
   Begin
        Write('Teclea hasta que numero deseas sumar: ');
        Readln(N);
   End;
   Function Suma(N:integer):integer;
   Var
      i,total:integer;   //Variables locales
   Begin
        i:=1;
        total:=0;
        While (i<=N) do
             Begin
                  total:=total+i;
                  i:=i+1;
             End;
        suma:=total;
        Writeln('La suma es: ',total);
   end;
   Begin
        Clrscr;
        Bienvenida;
        Lectura;
        suma(N);
Readln;
End.
