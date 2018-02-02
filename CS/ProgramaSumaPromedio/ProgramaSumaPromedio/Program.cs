using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProgramaSumaPromedio
{
    class Program
    {
        static void Main(string[] args)
        {
            float num1, num2, num3, num4, suma, promedio;
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
            Console.Write("Ingresa el cuarto numero: ");
            linea = Console.ReadLine();
            num4 = float.Parse(linea);
            suma = num1 + num2 + num3 + num4;
            promedio = suma / 4;
            Console.Write("La suma total es: ");
            Console.WriteLine(suma);
            Console.Write("El promedio total es: ");
            Console.Write(promedio);
            Console.ReadKey();
        }
    }
}
