{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 22 de febrero de 2016
 Asutno: Programa que identifica la edad menor
}
Program Edad_menor;
Uses crt;
Var
   A,B,C,MENOR:integer;
Begin
     textbackground(white);
     Clrscr;
     textcolor(red);
     Writeln('                             ***EDAD MENOR***');
     textcolor(black);
     write('Teclea edad A:');
     readln(A);
     textcolor(black);
     write('Teclea edad B:');
     readln(B);
     textcolor(black);
     write('Teclea edad C:');
     readln(C);
     if (A<=B) and (A<=C) then
        MENOR:=A
     else
         if (B<=A) and (B<=C) then
            MENOR:=B
         else
            MENOR:=C;
     textcolor(cyan);
     writeln('La edad menor es:',MENOR);
     Readln;
end.