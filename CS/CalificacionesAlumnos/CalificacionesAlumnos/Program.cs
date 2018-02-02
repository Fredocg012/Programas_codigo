using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CalificacionesAlumnos
{
    class Program
    {
        static void Main(string[] args)
        {
            int nota, x, mayores, menores;
            string linea;
            x = 1;
            mayores = 0;
            menores = 0;
            while (x <= 10)
                  {
                   Console.Write("Ingresa la calificacion: ");
                   linea = Console.ReadLine();
                   nota = int.Parse(linea);
                   if (nota >= 7)
                      {
                       mayores = mayores + 1;
                      }
                   else
                       {
                        menores = menores + 1;
                       }
                   x = x + 1;
                  }
            Console.Write("Alumnos con notas MAYORES o IGUALES a 7: ");
            Console.WriteLine(mayores);
            Console.Write("Alumnos con notas MENORES a 7: ");
            Console.Write(menores);
            Console.ReadKey();
        }
    }
}
