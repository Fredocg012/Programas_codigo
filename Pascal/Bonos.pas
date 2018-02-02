{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 22 de febrero de 2016
 Asunto: Programa que otorga un bono a trabajadores
}
Program Bonos;
Uses crt;
Const
     factor1=1000;
     factor2=0;
Var
   sueldo,diastrabajo,Bono:real;
Begin
     textbackground(white);
     Clrscr;
     Textcolor(red);
     Writeln('                             *** OTORGA BONOS ***');
     Writeln(' ');
     Textcolor(black);
     Writeln('*BIENVENIDO TRABAJADOR*');
     writeln(' ');
     Textcolor(magenta);
     Write('Teclea tu sueldo:');
     readln(sueldo);
     Textcolor(magenta);
     Write('Teclea los dias que trabajaste:');
     readln(diastrabajo);
     if (sueldo>=3000) and (diastrabajo>=15) then
        Begin
        Bono:=factor1;
        writeln('Tu bono otorgado es de: ',Bono:4:2);
        end
     else
         if (sueldo>=3000) and (diastrabajo<15) then
         Begin
         Bono:=factor2;
         writeln('Lo sentimos, no podemos darte el bono');
         end
     else
         if (sueldo<3000) and (diastrabajo>=15) then
         Begin
         Bono:=factor2;
         writeln('Lo sentimos, no podemos darte el bono');
         end;
     writeln(' ');
     Textcolor(cyan);
     writeln('                            **** HASTA LUEGO ****');
     readln;
end.
