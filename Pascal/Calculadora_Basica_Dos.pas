{Autor: Jesus Adrian Rosas Martinez
 Fecha: 28 de Marzo de 2016
 Asunto: Calculadora B sica en programaci¢n modular
}
Program Calculadora_Basica;
Uses crt;
Var
   A,B,R:real;
   signo:char;
   Procedure Bienvenida;
   Begin
        Writeln('                         ****CALCULADORA BASICA****');
        Writeln(' ');
        Writeln('                                  ** MENU **');
        Writeln(' ');
        Writeln('                                   + suma');
        Writeln('                                   - resta');
        Writeln('                               * multiplicacion');
        Writeln('                                  / division');
        Writeln(' ');
        Writeln(' ');
   End;
   Procedure Opcion;
      Begin
        Write('  Teclea el signo de la operacion a realizar segun el menu: ');
        Readln(signo);
      End;
   Procedure Lectura;
      Begin
        Write('  Teclea el valor de A: ');
        Readln(A);
        Write('  Teclea el valor de B: ');
        Readln(B);
      End;
   Procedure Suma;
      Begin
        R:=A+B;
        Writeln('  El resultado de la suma A+B es: ',R:6:2);
        Writeln(' ');
        Writeln('                              ----HASTA PRONTO----');
      End;
   Procedure Resta;
      Begin
        R:=A-B;
        Writeln('  El resultado de la resta A-B es: ',R:6:2);
        Writeln(' ');
        Writeln('                              ----HASTA PRONTO----');
      End;
   Procedure Multiplicacion;
      Begin
        R:=A*B;
        Writeln('  El resultado de la multiplicacion A*B es: ',R:6:2);
        Writeln(' ');
        Writeln('                              ----HASTA PRONTO----');
      End;
   Procedure Division;
      Begin
        R:=A/B;
        Writeln('  El resultado de la division A/B es: ',R:6:2);
        Writeln(' ');
        Writeln('                              ----HASTA PRONTO----');
      End;
   Procedure Error;
   Begin
        Writeln(' ');
        Writeln('         ERROR! VERIFICA EL SIGNO DE LA OPERACION A REALIZAR (+,-,*,/)');
   end;
Begin
     Clrscr;
     Bienvenida;
     Opcion;
     Lectura;
     Case signo of
     '+':Begin
              Suma;
     end;
     '-':Begin
              Resta;
     end;
     '*':Begin
              Multiplicacion;
     end;
     '/':Begin
              Division;
     end;
     else
         Error;
     end;
Readln;
End.