using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TresNumerosIguales
{
    class Program
    {
        static void Main(string[] args)
        {
            float num1, num2, num3, suma, producto;
            string linea;
            Console.Write("Ingresa el primer numero: ");
            linea = Console.ReadLine();
            num1 = float.Parse(linea);
            Console.Write("Ingresa el segundo numero: ");
            linea = Console.ReadLine();
            num2 = float.Parse(linea);
            Console.Write("Ingresa el tercer numero: ");
            linea = Console.ReadLine();
            num3 = float.Parse(linea);
            if (num1 == num2 && num2 == num3)
               {
                suma = num1 + num2;
                producto = suma * num3;
                Console.Write("Los numeros ingresados son iguales, por lo tanto, el resultado es: ");
                Console.Write(producto);
               }
            else
                {
                 Console.Write("Los numeros ingresados no son iguales");
                }
            Console.ReadKey();
        }
    }
}
