{ALUMNO: Jesus Adrian Rosas Martinez
 FECHA: 24 de Febrero de 2016
 ASUNTO: Programa que muestra los meses especiales
}
Program meses_especiales;
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
        4..8:Begin
             writeln('Meses calurosos');
             writeln('Te recomiendo visitar las playas mexicanas');
        end;
        9,12:Begin
             writeln('Meses de fiesta');
             writeln('No tomes riesgos');
        end;
     10:writeln('El mes es: Octubre');
        11:writeln('El mes es: Noviembre');
     else
         writeln('ERROR!, Teclea numeros entre 1 y 12');
     end;
     readln;
end.
