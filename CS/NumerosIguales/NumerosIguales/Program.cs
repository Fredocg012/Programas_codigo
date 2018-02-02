using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NumerosIguales
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, num3, suma, producto;
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
            suma = num1 + num2;
            producto = suma * num3;
            if (num1 == num2 && num2 == num3)
               {
                Console.Write("La suma del primer numero y segundo es: ");
                Console.WriteLine(suma);
                Console.Write("La suma del primer y segundo numero, por el tercer numero es: ");
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
