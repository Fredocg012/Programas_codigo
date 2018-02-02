using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PrimerTrimesteAño
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
            Console.Write("Ingresa el año: ");
            linea = Console.ReadLine();
            año = int.Parse(linea);
            if (mes == 1 || mes == 2 || mes ==3)
               {
                Console.Write("La fecha ingresada corresponde al primer trimestre del año");
               }
            Console.ReadKey();
        }
    }
}
