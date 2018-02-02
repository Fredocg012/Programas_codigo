{Alumno: Jesus Adrian Rosas Martinez
 Fecha: 10 de febrero de 2016
 Asunto: Proyecto 1
}
Program Proyecto_1;
Uses crt;
Const
     mensaje='BIENVENIDO';
Var
   R,T,V,B,A,P:real;
   nombre1:string;
   nombre2:string;
   apellidop:string;
   apellidom:string;
Begin
     Clrscr;
     writeln(Mensaje);
     writeln('**********');
     writeln(' ******** ');
     writeln('  ******  ');
     writeln('   ****   ');
     writeln('    **    ');
     write('Teclea tu primer nombre:');
     readln(nombre1);
     write('Teclea tu segundo nombre:');
     readln(nombre2);
     write('Teclea tu apellido paterno:');
     readln(apellidop);
     write('Teclea tu apellido materno:');
     readln(apellidom);
     writeln('Hola: ',nombre1,' ',nombre2,' ',apellidop,' ',apellidom);
     write('Teclea el valor de R:');
     readln(R);
     write('Teclea el valor de T:');
     readln(T);
     write('Teclea el valor de V;');
     readln(V);
     write('Teclea el valor de B:');
     readln(B);
     write('Teclea el valor de A;');
     readln(A);
     P:=((R*T)/(V-B))-(A/sqr(V));
     writeln(nombre1,', el valor de P es:',P:6:2);
     readln;
end.