using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PositivoNuloNegativo
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1;
            string linea;
            Console.Write("Ingrese un numero entero: ");
            linea = Console.ReadLine();
            num1 = int.Parse(linea);
            if (num1 == 0)
               {
                Console.Write("El numero ingresado es nulo");
               }
            else
                {
                 if (num1 > 0)
                    {
                     Console.Write("El numero ingresado es positivo");
                    }
                 else
                     {
                      Console.Write("El numero ingresado es negativo");
                     }
                }
            Console.ReadKey();
        }
    }
}
