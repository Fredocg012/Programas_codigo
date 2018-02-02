{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 1 de Abril de 2016
 Asunto: Programa que muestra el factorial de un numero
}
Program Factorial_modular;
Uses crt;
Var
   N:integer;  //Variables globales
   Procedure Bienvenida;
   Begin
        Writeln('                                    *** NUMERO FACTORIAL ***');
   End;
   Procedure Lectura;
   Begin
        Write('   Teclea el numero: ');
        Readln(N);
   End;
   Function Factorial(N:integer):real;
   Var
      i:integer;      //Variables locales
      resultado:real;
   Begin
        resultado:=1;
        i:=1;
        While (i<=N) do
             Begin
                  resultado:=resultado*i;
                  i:=i+1;
             End;
        Factorial:=resultado;
        Writeln('   El factorial es: ',resultado:6:0);
   End;
Begin
     Textbackground(white); //Color de pantalla
  Clrscr;
     Textcolor(black); //Color de letra
  Bienvenida;
     Writeln(' '); //Espaciado
     Writeln(' '); //Espaciado
  Lectura;
     Writeln(' '); //Espaciado
     Textcolor(red); //Color de letra
  Factorial(N);
     Writeln(' '); //Espaciado
     Writeln(' '); //Espaciado
     Textcolor(black); //Color de letra
     Writeln('                                        **HASTA PRONTO**'); //Despedida
Readln;

End.