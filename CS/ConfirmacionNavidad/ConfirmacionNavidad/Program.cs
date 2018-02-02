using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConfirmacionNavidad
{
    class Program
    {
        static void Main(string[] args)
        {
            int dia, mes, año;
            string linea;
            Console.Write("Ingresa el numero de dia: ");
            linea = Console.ReadLine();
            dia = int.Parse(linea);
            Console.Write("Ingresa el numero de mes: ");
            linea = Console.ReadLine();
            mes = int.Parse(linea);
            Console.Write("Ingresa el numero de año: ");
            linea = Console.ReadLine();
            año = int.Parse(linea);
            if (dia == 25 && mes ==12)
               {
                Console.Write("DIA DE NAVIDAD");
               }
            else
                {
                Console.Write("Lamentablemente, hoy NO es navidad");
                }
            Console.ReadKey();
        }
    }
}
