{ALUMNO: Jesus Adrian Rosas Martinez
 FECHA: 06 de Marzo de 2016
 ASUNTO: Programa que te muestra el mes dos veces
}
Program Meses;
Uses crt;
Var
        mes:integer;
        respuesta:char;
BEGIN
        Textbackground(white);
        Clrscr;
        Textcolor(red);
        Writeln('                                                **MESES DEL A¥O**');
        Textcolor(black);
        Write('Teclea el numero del mes: ');
        readln(mes);
        respuesta:='s';
        Textcolor(magenta);
        while (respuesta='s') do
        begin
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
        Textcolor(green);
        writeln('ERROR!, TECLEA NUMEROS ENTRE 1 Y 12');
        END;
        Textcolor(black);
        WRITE('Deseas ver otro mes? s/n: ');
        READLN(RESPUESTA);
        WRITE('Teclea el numero del mes: ');
        READLN(MES);
        END;
        READLN;
END.
