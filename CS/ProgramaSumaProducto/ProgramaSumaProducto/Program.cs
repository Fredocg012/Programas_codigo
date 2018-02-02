using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProgramaSumaProducto
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, producto, suma;
            string linea;
            Console.Write("Ingresa el primer numero: ");
            linea = Console.ReadLine();
            num1 = int.Parse(linea);
            Console.Write("Ingresa el segundo numero: ");
            linea = Console.ReadLine();
            num2 = int.Parse(linea);
            suma = num1 + num2;
            producto = num1 * num2;
            Console.Write("El resultado de la suma es: ");
            Console.WriteLine(suma);
            Console.Write("El resultado de la multiplicacion es: ");
            Console.Write(producto);
            Console.ReadKey();
        }
    }
}
