using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WhileUsuario
{
    class Program
    {
        static void Main(string[] args)
        {
            int n, x;
            string linea;
            x = 1;
            Console.Write("Ingresa un valor entero: ");
            linea = Console.ReadLine();
            n = int.Parse(linea);
            while (x <= n)
                  {
                   Console.Write(x);
                   Console.Write(" - ");
                   x = x + 1;
                  }
            Console.ReadKey();
        }
    }
}
