using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NumeroDistinto0
{
    class Program
    {
        static void Main(string[] args)
        {
            float num1, num2;
            string linea;
            Console.Write("Ingresa el numero: ");
            linea = Console.ReadLine();
            num1 = float.Parse(linea);
            if (num1 != 0)
               {
                Console.Write("El numero es diferente de 0, por lo tanto, el resultado es: ");
                num2 = num1 * 10;
                Console.Write(num2);
               }
            else
               {
                Console.Write("El numero ingresado es igual a 0");
               }
            Console.ReadKey();
        }
    }
}
