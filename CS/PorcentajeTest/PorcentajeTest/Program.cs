using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PorcentajeTest
{
    class Program
    {
        static void Main(string[] args)
        {
            int preguntasRealizadas, preguntasContestadas, nivel;
            string linea;
            Console.Write("Ingrese el total de preguntas realizadas: ");
            linea = Console.ReadLine();
            preguntasRealizadas = int.Parse(linea);
            Console.Write("Ingrese el total de preguntas contestadas correctamente: ");
            linea = Console.ReadLine();
            preguntasContestadas = int.Parse(linea);
            nivel = (preguntasContestadas * 100) / preguntasRealizadas;
            Console.Write("Nivel de la persona: ");
            if (nivel >= 90)
               {
                Console.Write("MAXIMO");
               }
            else
                {
                 if (nivel >= 75)
                    {
                     Console.Write("MEDIO");
                    }
                 else
                     {
                      if (nivel >= 50)
                         {
                          Console.Write("REGULAR");
                         }
                      else
                          {
                           Console.Write("FUERA DE NIVEL");
                          }
                     }
                }
            Console.ReadKey();
        }
    }
}
