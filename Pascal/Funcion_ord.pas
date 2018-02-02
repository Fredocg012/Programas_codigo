{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 3 de febrero de 2016
 Asunto: Ejemplo de la funcion Ord
}
Program Funcion_Ord;
Uses crt;
Var
   L1,L2,L3,L4,L5:Char;
Begin
     Textbackground(cyan);
     Clrscr;
     textcolor(magenta);
     writeln('                          *EJEMPLO DE LA FUNCION ORD*');
     textcolor(black);
     writeln('Teclea un nombre de 5 letras, tecleando letra por letra:');
     textcolor(yellow);
     write('Teclea Letra 1:');
     readln(L1);
     write('Teclea Letra 2:');
     readln(L2);
     write('Teclea Letra 3:');
     readln(L3);
     write('Teclea Letra 4:');
     readln(L4);
     write('Teclea Letra 5:');
     readln(L5);
     Writeln('El codigo ASCII es:');
     writeln('Para L1: ',(ord(L1)));
     writeln('Para L2: ',(ord(L2)));
     writeln('Para L3: ',(ord(L3)));
     writeln('Para L4: ',(ord(L4)));
     writeln('Para L5: ',(ord(L5)));
     Readln;
end.
