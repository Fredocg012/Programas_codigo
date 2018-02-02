using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OperadoresMatematicos
{
    class Program
    {
        static void Main(string[] args)
        {
            float num1, num2, suma, diferencia, producto, division;
            string linea;
            Console.Write("Ingresa el primer numero: ");
            linea = Console.ReadLine();
            num1 = float.Parse(linea);
            Console.Write("Ingresa el segundo numero: ");
            linea = Console.ReadLine();
            num2 = float.Parse(linea);
            if (num1 > num2)
               {
                suma = num1 + num2;
                diferencia = num1 - num2;
                Console.Write("La suma total es: ");
                Console.WriteLine(suma);
                Console.Write("La resta total es: ");
                Console.Write(diferencia);
               }
            else
               {
                producto = num1 * num2;
                division = num1 / num2;
                Console.Write("El producto total es; ");
                Console.WriteLine(producto);
                Console.Write("La división entre el primer numero sobre el segundo es: ");
                Console.Write(division);
               }
            Console.ReadKey();  
        }
    }
}
