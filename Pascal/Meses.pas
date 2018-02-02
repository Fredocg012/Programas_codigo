{ALUMNO: Jesus Adrian Rosas Martinez
 FECHA: 24 de Febrero de 2016
 ASUNTO: Programa que muestra los meses del a¤o
}
Program meses;
Uses crt;
Var
   numeromes:integer;
Begin
     Clrscr;
     Writeln('***MESES DEL A¥O***');
     Write('Teclea el numero del mes:');
     readln(numeromes);
     case numeromes of
        1:writeln('El mes es: Enero');
        2:writeln('El mes es: Febrero');
        3:writeln('El mes es: Marzo');
        4:writeln('El mes es: Abril');
        5:writeln('El mes es: Mayo');
        6:writeln('El mes es: Junio');
        7:writeln('El mes es: Julio');
        8:writeln('El mes es: Agosto');
        9:writeln('El mes es: Septiembre');
        10:writeln('El mes es: Octubre');
        11:writeln('El mes es: Noviembre');
        12:writeln('El mes es: Diciembre');
     else
         writeln('ERROR!, Teclea numeros entre 1 y 12');
     end;
     readln;
end.