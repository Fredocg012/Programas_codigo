using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProgramaSumaProducto2
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, num3, num4, suma, producto;
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
            Console.Write("Ingresa el cuarto numero: ");
            linea = Console.ReadLine();
            num4 = int.Parse(linea);
            suma = num1 + num2;
            producto = num3 * num4;
            Console.Write("La suma de los dos primeros numeros es: ");
            Console.WriteLine(suma);
            Console.Write("El producto del tercer y cuarto numero es: ");
            Console.Write(producto);
            Console.ReadKey();
        }
    }
}
