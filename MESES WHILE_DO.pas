{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 02 de marzo de 2016
 Asunto: PROGRAMA QUE VUELVA A PREGUNTAR AL USUARIO EL MES
}
PROGRAM MESES;
USES CRT;
VAR
        MES:INTEGER;
        respuesta:char;
BEGIN
     Textbackground(white);
     CLRSCR;
     textcolor(red);
     WRITELN('                                    **MESES DEL A•O**');
     writeln(' ');
     writeln(' ');
     textcolor(black);
     WRITE('Teclea el numero del mes: ');
          READLN(MES);
          respuesta:='s';
      case mes of
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
      writeln(' ');
      textcolor(red);
      writeln('                              ERROR!, TECLEA NÈMEROS ENTRE 1 Y 12');
      WRITELN(' ');
      textcolor(cyan);
      writeln('                                     *** HASTA LUEGO ***');
      END;
   while (respuesta='s') do
   begin
   writeln(' ');
   textcolor(black);
   WRITE('®Deseas ver otro mes? S/N: ');
        READLN(RESPUESTA);
        writeln(' ');
        WRITE('TECLEA EL NÈMERO DEL MES: ');
        READLN(MES);
        case mes of
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
        writeln(' ');
        textcolor(red);
        writeln('                           ERROR!, TECLEA NÈMEROS ENTRE 1 Y 12');
        WRITELN(' ');
        textcolor(cyan);
        writeln('                                   *** HASTA LUEGO ***');
        END;
   end;
 READLN;
END.
