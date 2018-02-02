using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NumeroMayor
{
    class Program
    {
        static void Main(string[] args)
        {
            float num1, num2;
            string linea;
            Console.Write("Ingresa el primer numero: ");
            linea = Console.ReadLine();
            num1 = float.Parse(linea);
            Console.Write("Ingresa el segundo numero: ");
            linea = Console.ReadLine();
            num2 = float.Parse(linea);
            Console.Write("El mayor de los dos numeros es: ");
            if (num1>num2)
               {
                Console.Write(num1);
               }
            else
               {
                Console.Write(num2);
               }
            Console.ReadKey();
        }
    }
}
