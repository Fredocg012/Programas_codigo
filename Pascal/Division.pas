{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 31 de Febrero de 2016
 Asunto: Programa que calcula el porcentaje de un numero
}
Program Porcentaje_num;
Uses crt;
Var
   nume1,nume2,total:real;
Begin
     textbackground(cyan);
     textcolor(yellow);
     Clrscr;
     Writeln('                                        **PORCENTAJE DE UN NUMERO**');
     writeln(' ');
     writeln(' ');
     writeln(' ');
     write('   Teclea el numero a evaluar: ');
     readln(nume1);
     writeln(' ');
     write('   Teclea el porcentaje a calcular ( % ): ');
     readln(nume2);
     writeln(' ');
     writeln(' ');
     if (nume2>0) then
        Begin
        total:=(nume1*nume2)/100;
        writeln(' ');
        writeln(' ');
        writeln('   El resultado es: ',total:6:2);
     writeln(' ');
     writeln(' ');
     Writeln('                                              **HASTA PRONTO**');
        end
     Else
        Writeln('                     El porcentaje en negativo no existe, Intenta nuevamente!');

     Readln;
end.


