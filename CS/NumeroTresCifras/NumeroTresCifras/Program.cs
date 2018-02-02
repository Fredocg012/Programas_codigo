using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NumeroTresCifras
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1;
            string linea;
            Console.Write("Ingrese un numero entero positivo de hasta tres digitos: ");
            linea = Console.ReadLine();
            num1 = int.Parse(linea);
            if (num1 < 0)
               {
                Console.Write("ERROR, EL NUMERO INGRESADO NO ES POSITIVO");
               }
            else
                {
                 if (num1 < 10)
                    {
                     Console.Write("El numero ingresado tiene un digito");
                    }
                 else
                     {
                      if (num1 < 100)
                         {
                          Console.Write("El numero ingresado tiene dos digitos");
                         }
                      else
                          {
                           if (num1 < 1000)
                              {
                               Console.Write("El numero ingresado tiene tres digitos");
                              }
                           else
                               {
                                Console.Write("ERROR, EL NUMERO INGRESADO TIENE MAS DE 3 DIGITOS");
                               }
                          }
                     }   
                }
            Console.ReadKey();
        }
    }
}
