using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MayorDeTresNumeros2
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
            Console.Write("El numero mayor es: ");
            if (num1 > num2 && num1 > num3)
               {
                Console.Write(num1);
               }
            else
                {
                 if (num2 > num3)
                    {
                     Console.Write(num2);
                    }
                 else
                     {
                      Console.Write(num3);
                     }
                }
            Console.ReadKey();
        }
    }
}
