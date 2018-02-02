using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PromedioAlumno2
{
    class Program
    {
        static void Main(string[] args)
        {
            float nota1, nota2, nota3, promedio;
            string linea;
            Console.Write("Ingresa la primera calificacion: ");
            linea = Console.ReadLine();
            nota1 = float.Parse(linea);
            Console.Write("Ingresa la segunda calificacion: ");
            linea = Console.ReadLine();
            nota2 = float.Parse(linea);
            Console.Write("Ingresa la tercera calificacion: ");
            linea = Console.ReadLine();
            nota3 = float.Parse(linea);
            promedio = (nota1 + nota2 + nota3) / 3;
            if (promedio >= 7)
               {Console.Write("Alumno Aprobado");}
            else
               {
                if (promedio >= 4)
                   {
                    Console.Write("Alumno Regular");
                   }
                else
                    {
                     Console.Write("Alumno Reprobado");
                    }
               }
            Console.ReadKey();
        }
    }
}
