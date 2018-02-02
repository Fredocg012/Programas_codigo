{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 07 de Marzo de 2016
 Asunto: Ciclo Repeat until
}
Program raizc;
Uses crt;
Var
   num,raiz:real;
Begin
     Clrscr;
     Write('Escribe el valor del numero: ');
     Readln(num);
     if num<0 then
     Writeln('No se puede obtener la raiz cuadrada')
     else
     Begin
     raiz:=sqrt(num);
     Writeln('Resultado = ',raiz:2:2);
     end;
Readln;
end.
