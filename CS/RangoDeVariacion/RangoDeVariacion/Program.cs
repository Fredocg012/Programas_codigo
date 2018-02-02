using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RangoDeVariacion
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, num3;
            string linea;
            Console.Write("Ingresa el primer numero: ");
            linea = Console.ReadLine();
            num1 = int.Parse(linea);
            Console.Write("Ingresa el segundo numero: ");
            linea = Console.ReadLine();
            num2 = int.Parse(linea);
            Console.Write("Ingresa el tercer numero: ");
            linea = Console.ReadLine();
            num3 = int.Parse(linea);
            if ( num1 > num2 && num1 > num3)
               {
                if (num2 > num3)
                   {
                    Console.Write("El mayor de los numeros ingresados es: ");
                    Console.WriteLine(num1);
                    Console.Write("El menor de los numeros ingresados es: ");
                    Console.Write(num3);
                   }
                else
                    {
                     Console.Write("El mayor de los numeros ingresados es: ");
                     Console.WriteLine(num1);
                     Console.Write("El menor de los numeros ingresados es: ");
                     Console.Write(num2);
                    }
                }
            else
                {
                 if (num2 > num1 && num2 > num3)
                    {
                     if (num1 > num3)
                        {
                         Console.Write("El mayor de los numeros ingresados es: ");
                         Console.WriteLine(num2);
                         Console.Write("El menor de los numeros ingresados es: ");
                         Console.Write(num3);
                        }
                     else
                         {
                          Console.Write("El mayor de los numeros ingresados es: ");
                          Console.WriteLine(num2);
                          Console.Write("El menor de los numeros ingresados es: ");
                          Console.Write(num1);
                         }
                     }
                 else
                     {
                      if (num3 > num1 && num3 > num2)
                         {
                          if (num1 > num2)
                             {
                              Console.Write("El mayor de los numeros ingresados es: ");
                              Console.WriteLine(num3);
                              Console.Write("El menor de los numeros ingresados es: ");
                              Console.Write(num2);
                             }
                          else
                              {
                               Console.Write("El mayor de los numeros ingresados es: ");
                               Console.WriteLine(num3);
                               Console.Write("El menor de los numeros ingresados es: ");
                               Console.Write(num1);
                              }
                         }
                      else
                          {
                           Console.Write("ERROR, AL MENOS DOS NUMEROS SON IGUALES");
                          }
                     }
                }
            Console.ReadKey();
        }
    }
}
