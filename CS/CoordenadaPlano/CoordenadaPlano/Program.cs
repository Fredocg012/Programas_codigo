using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CoordenadaPlano
{
    class Program
    {
        static void Main(string[] args)
        {
            int x, y;
            string linea;
            Console.Write("Ingresa la coordenada x: ");
            linea = Console.ReadLine();
            x = int.Parse(linea);
            Console.Write("Ingresa la coordenada y: ");
            linea = Console.ReadLine();
            y = int.Parse(linea);
            if (x > 0 && y > 0)
               {
                Console.Write("El punto ingresado se ubica en el PRIMER CUADRANTE.");
               }
            else
                {
                 if (x < 0 && y > 0)
                    {
                     Console.Write("El punto ingresado se ubica en el SEGUNDO CUADRANTE");
                    }
                 else
                     {
                      if (x > 0 && y < 0)
                         {
                          Console.Write("El punto ingresado se ubica en el CUARTO CUADRANTE");
                         }
                      else
                          {
                           if (x < 0 && y < 0)
                              {
                               Console.Write("El punto ingresado se ubica en el TERCER CUADRANTE");
                              }
                           else
                               {
                                Console.Write("ERROR, INGRESAR COORDENADAS DISTINTAS DE CERO");
                               }
                          } 
                      }
                 }
            Console.ReadKey();
        }
    }
}
