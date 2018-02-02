using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PromedioAlumno
{
    class Program
    {
        static void Main(string[] args)
        {
            float num1, num2, num3, promedio;
            string linea;
            Console.Write("Ingresa la primera calificacion: ");
            linea = Console.ReadLine();
            num1 = float.Parse(linea);
            Console.Write("Ingresa la segunda calificacion: ");
            linea = Console.ReadLine();
            num2 = float.Parse(linea);
            Console.Write("Ingresa la tercera calificacion: ");
            linea = Console.ReadLine();
            num3 = float.Parse(linea);
            promedio = (num1 + num2 + num3) / 3;
            if (promedio >= 7)
               {
                Console.Write("Alumno APROBADO");
               }
            else
               {
                Console.Write("Alumno REPROBADO");
               }
            Console.ReadKey();
        }
    }
}
