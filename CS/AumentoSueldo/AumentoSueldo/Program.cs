using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AumentoSueldo
{
    class Program
    {
        static void Main(string[] args)
        {
            int años;
            float sueldo, aumento, porcentaje;
            string linea;
            Console.Write("Ingresa el sueldo: ");
            linea = Console.ReadLine();
            sueldo = float.Parse(linea);
            Console.Write("Ingresa los años de antigüedad: ");
            linea = Console.ReadLine();
            años = int.Parse(linea);
            Console.Write("EL sueldo a pagar es: ");
            if (sueldo < 500 && años >= 10)
               {
                porcentaje = (sueldo * 20) / 100;
                aumento = sueldo + porcentaje;
                Console.Write(aumento);
               }
            else
                {
                 if (sueldo < 500 && años < 10)
                    {
                     porcentaje = (sueldo * 5) / 100;
                     aumento = sueldo + porcentaje;
                     Console.Write(aumento);
                    }
                 else
                     {
                      Console.Write(sueldo);
                     }
                }
            Console.ReadKey();
        }
    }
}
