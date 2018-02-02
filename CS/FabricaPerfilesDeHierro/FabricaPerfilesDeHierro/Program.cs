using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FabricaPerfilesDeHierro
{
    class Program
    {
        static void Main(string[] args)
        {
            int cantidad, x, n;
            float largo;
            string linea;
            x = 1;
            cantidad = 0;
            Console.Write("Ingresa la cantidad de piezas a procesar: ");
            linea = Console.ReadLine();
            n = int.Parse(linea);
            while (x <= n)
                  {
                   Console.Write("Ingrese la longitud de cada perfil: ");
                   linea = Console.ReadLine();
                   largo = float.Parse(linea);
                   if (largo >= 120 && largo <= 130)
                      {
                       cantidad = cantidad + 1;
                      }
                   x = x + 1;
                  }
            Console.Write("Cantidad de piezas aptas: ");
            Console.Write(cantidad);
            Console.ReadKey();
        }
    }
}
