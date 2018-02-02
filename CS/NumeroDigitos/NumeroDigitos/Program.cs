using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NumeroDigitos
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1;
            string linea;
            Console.Write("Ingresa un numero: ");
            linea = Console.ReadLine();
            num1 = int.Parse(linea);
            if (num1<10)
               {
                Console.Write("El numero ingresado tiene un digito");
               }
            else
               {
                if (num1 < 100)
                   {
                    Console.Write("El numero ingresado tiene dos digitos");
                   }
               }
            Console.ReadKey();
        }
    }
}
