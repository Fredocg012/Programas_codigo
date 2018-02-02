using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PromedioConWhile
{
    class Program
    {
        static void Main(string[] args)
        {
            int x, suma, valor, promedio;
            string linea;
            x = 1;
            suma = 0;
            while (x <= 10)
                  {
                   Console.Write("Ingresa un valor: ");
                   linea = Console.ReadLine();
                   valor = int.Parse(linea);
                   suma = suma + valor;
                   x = x + 1;
                  }
            promedio = suma / 10;
            Console.Write("La suma total es: ");
            Console.WriteLine(suma);
            Console.Write("El promedio es: ");
            Console.Write(promedio);
            Console.ReadKey();
        }
    }
}
