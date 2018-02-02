using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MenoresDeDiez
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
            if (num1 < 10 && num2 <10 && num3 <10)
               {
                Console.Write("TODOS LOS NUMEROS SON MENORES A DIEZ");
               }
            else
                {
                 Console.Write("AL MENOS UN NUMERO ES MAYOR O IGUAL A DIEZ");
                }
            Console.ReadKey();
        }
    }
}
