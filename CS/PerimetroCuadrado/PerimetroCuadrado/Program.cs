﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PerimetroCuadrado
{
    class Program
    {
        static void Main(string[] args)
        {
            float lado, perimetro;
            string linea;
            Console.Write("Ingresa el lado del cuadrado: ");
            linea = Console.ReadLine();
            lado = float.Parse(linea);
            perimetro = lado * lado * lado * lado;
            Console.Write("El perimetro del cuadrado es: ");
            Console.Write(perimetro);
            Console.ReadKey();
        }
    }
}
