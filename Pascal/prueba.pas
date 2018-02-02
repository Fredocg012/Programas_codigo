Program procedimiento;
Uses crt;
Var
   A,B,resultado:real;
Procedure lectura;
Begin
     write('introdusca el primer numero: ');
     readln(A);
     writeln('introdusca el segundo numero: ');
     readln(B);
end;
Procedure suma;
Begin
     resultado:=A+B;
     writeln('la suma es: ',resultado:6:2);
end;

Begin
     clrscr;
     lectura;
     suma;
readln;
end.