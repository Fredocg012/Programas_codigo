{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 28 de Febrero de 2016
 Asunto:Calculadora b sica
}
Program calculadora_basica ;
Uses crt;
Var
    A,B,resultado:real;
    signo:char;
Begin
      Textbackground(white);
      Clrscr;
      textcolor(black);
      Writeln(' ');
      Writeln('                              ***CALCULADORA BASICA***');
      Writeln(' ');
      Writeln(' ');
      textcolor(red);
      Writeln('                                        MENU');
      Writeln(' ');
      textcolor(magenta);
      Writeln('                                      + SUMA');
      Writeln('                                      - RESTA');
      Writeln('                                  * MULTIPLICACION');
      Writeln('                                     / DIVISION');
      Writeln(' ');
      Writeln(' ');
      textcolor(black);
      Write('Teclea el signo de la operacion a realizar: ');
      readln(signo);
      write('Teclea el valor de A: ');
      readln(A);
      write('Teclea el valor de B: ');
      readln(B);
   Case signo of
   '+':Begin
            resultado:=A+B;
            writeln(' ');
            Writeln('El resultado de la suma A+B es:',resultado:6:2);
            writeln(' ');
            textcolor(cyan);
            writeln('                                  ** HASTA PRONTO **');
            end;
   '-':Begin
            resultado:=A-B;
            writeln(' ');
            textcolor(black);
            writeln('El resultado de la resta A-B es:',resultado:10:2);
            writeln(' ');
            textcolor(cyan);
            writeln('                                  ** HASTA PRONTO **');
            end;
   '*':Begin
            resultado:=A*B;
            writeln(' ');
            textcolor(black);
            writeln('El resultado de la multiplicacion A*B es:',resultado:10:2);
            writeln(' ');
            textcolor(cyan);
            writeln('                                  ** HASTA PRONTO **');
            end;
   '/':Begin
            resultado:=A/B;
            writeln(' ');
            textcolor(black);
            writeln('El resultado de la division A/B es:',resultado:10:2);
            writeln(' ');
            textcolor(cyan);
            writeln('                                  ** HASTA PRONTO **');
            end;
   else
        writeln(' ');
        textcolor(red);
        writeln('                          ERROR!,VERIFICA EL SIGNO (+,-,*,/)');
   end;
   readln;
   end.




