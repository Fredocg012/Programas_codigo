using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdvertenciaIguales
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
            if (num1 == num2)
               {
                Console.Write("ADVERTENCIA, LOS NUMEROS INGRESADOS SON IGUALES");
               }
            else
               {
                Console.Write("Los numeros ingresados son diferentes, falsa alarma");
               }
            Console.ReadKey();
        }
    }
}
