{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 2 de Marzo de 2016
 Asunto: Programa que muestra de la A a la F en c¢digo ASCII
}
Program CodigoForDown;
Uses crt;
Var
   i:integer;
Begin
     Clrscr;
     Writeln('** CODIGOS ASCII**');
     For i:=70 downto 65 do
        writeln(Chr(i));
     writeln('**ADIOS**');
     readln;
     end.
