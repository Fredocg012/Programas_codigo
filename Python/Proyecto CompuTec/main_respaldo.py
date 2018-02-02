#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,codecs,shutil
import sqlite3
from menus import *

def generar_ticket():
    f = codecs.open('ticket.txt', encoding='utf-8', mode='w+')
    f.write(u'                                        ......................................................................    \r\n')
    f.write(u'                                    ______________________________________________________________________________\r\n')
    f.write(u' \r\n')
    f.write(u'                                                                                                  ¤    ¤          \r\n')
    f.write(u'                                                                                           ■■■■ ¤        ¤ ■■■■   \r\n')
    f.write(u'                                    ▄▀▀▀ ▄▀▀▀▄ █▀▄ ▄▀█ █▀▀█ █  █ ▀▀█▀▀ █▀▀▀ ▄▀▀▀              ¤     ■■■    ¤      \r\n')
    f.write(u'                                    █    █   █ █  ▀  █ █▀▀▀ █  █   █   █▀▀  █           ████¤      █         ¤████\r\n')
    f.write(u'                                     ▀▀▀  ▀▀▀  ▀     ▀ ▀    ▀▀▀▀   ▀   ▀▀▀▀  ▀▀▀              ¤     ■■■    ¤      \r\n')
    f.write(u'                                                                                           ■■■■ ¤        ¤ ■■■■   \r\n')
    f.write(u'                                                                                                  ¤    ¤          \r\n')
    f.write(u' \r\n')
    f.write(u'                                                                    COMPUTEC SA DE CV                             \r\n')
    f.write(u' \r\n')
    f.write(u'                                                                  FACULTAD DE INGENIERÍA                          \r\n')
    f.write(u'                                                                CIUDAD UNIVERSITARIA, CDMX                        \r\n')
    f.write(u'                                                                        C.P. 04513                                \r\n')
    f.write(u'                                    ______________________________________________________________________________\r\n')
    f.write(u'                                        ----------------------------------------------------------------------    \r\n')
    f.write(u'                                                    GUARDA ESTE TICKET PARA POSIBLES DEVOLUCIONES                 \r\n')
    f.write(u'                                        ----------------------------------------------------------------------    \r\n')
    f.write(u'                                                               - Gracias por su compra -                          \r\n')
    f.write(u' \r\n')
    f.write(u'                                                            ATENCIÓN A CLIENTES: +96 5 555 599                    \r\n')
    f.write(u'                                                              Visítenos en: www.edupuma.info                      \r\n')
    f.write(u'                                    ______________________________________________________________________________\r\n')
    f.write(u'                                        ......................................................................    \r\n')
    f.write(u' \r\n')
    f.write(u'                                         Jesús Adrián Rosas Martínez                                              \r\n')
    f.write(u'                                         Juan Andrés Cruz                                                         \r\n')
    f.write(u' \r\n')
    f.write(u'                                                                                 ║█║|║║█║█║█║║|║║█║█║█║║|║║█║     \r\n')
    f.write(u'                                                                      Folio:     ║█║|║║█║█║█║║|║║█║█║█║║|║║█║     \r\n')
    f.write(u'                                                                                 ║█║|║║█║█║█║║|║║█║█║█║║|║║█║     \r\n')
    f.write(u'                                                                                  A 1 B 2 C 3 D 4 E 5 F 6 G 7     \r\n')
    f.write(u' \r\n')
    f.write(u'                                        ----------------------------------------------------------------------    \r\n')
    f.write(u'                                         Cliente: ')
    f.write("jesusdez"+'\r\n')
    f.write(u'                                        ----------------------------------------------------------------------    \r\n')
    f.write(u' \r\n')
    f.write(u'                                        ID    Cant   Producto(s)                   PU            Subtotal         \r\n')
    f.write(u' \r\n')
    f.close()

def ticket(id_prod,num_compras):
    fichero=open('ticket.txt','a')
    fichero.write("                                        "+str(id_prod[0])+"     ")
    fichero.write(str(num_compras)+"     ")
    con = sqlite3.connect('nombres.s3db')
    cursor = con.cursor()
    buscar = (int(id_prod[0]),)
    cursor.execute("SELECT costo FROM nombre WHERE id=?", buscar)
    for articulo in cursor:
        nom1=articulo
    con.close()
    nom2=nom1
    fichero.write(str(nom2[0])+"   ")
    con = sqlite3.connect('precios.s3db')
    cursor = con.cursor()
    buscar = (int(id_prod[0]),)
    cursor.execute("SELECT costo FROM costos WHERE id=?", buscar)
    for precio in cursor:
        prec1=precio
    con.close()
    prec2=prec1
    fichero.write(str(prec2[0])+"         ")
    mult=int(num_compras)*int(prec2[0])
    fichero.write(str(mult)+"\r\n")
    fichero.close()

def abrir_txt(nombre_txt):
    numero_txt=open(nombre_txt)
    print(numero_txt.read())
    numero_txt.close()

def ejemplo(limiteizq,limiteder,txt1):
    while True:
        try:
            os.system('cls')
            print "\n\n>> Productos disponibles:\n\n"
            abrir_txt(txt1)
            menu_opciones()
            sn=int(raw_input('\n\n\n>> Ingrese una opcion: '))
            if sn==1:
                print "\n\n"
                os.system('cls')
                print "\n\n>> Productos disponibles:\n\n"
                abrir_txt(txt1)
                opcion1=raw_input("\n\n>> Ingrese el ID del producto: ")
                if opcion1.isdigit():
                    opcion=int(opcion1)
                    if limiteizq<=opcion and opcion<=limiteder and opcion!=0 and opcion>0: 
                        con = sqlite3.connect('cantidades.s3db')
                        cursor = con.cursor()
                        buscar = (opcion,)
                        cursor.execute("SELECT cantidad FROM productos WHERE id=?", buscar)
                        for campo in cursor:
                            campo2=campo
                        con.close()
                        comprar=int(raw_input(">> Ingrese la cantidad a comprar: "))
                        compra=comprar
                        num=campo2[0]
                        comprar2=int(num)
                        while True:
                            try:
                                if comprar2>=comprar and comprar>0 and comprar!=0: 
                                    comprar3=str(comprar2-comprar)
                                    con = sqlite3.connect('cantidades.s3db')
                                    cursor = con.cursor()
                                    cursor.execute("UPDATE productos SET cantidad= '"+comprar3+"' WHERE id=?",buscar)
                                    con.commit()
                                    con.close()
                                    ticket(buscar,compra)
                                    print '\nCompra realizada, presiona "enter" para continuar ... ',
                                    repetir=0
                                    raw_input()
                                    ejemplo(limiteizq,limiteder,txt1)
                                    break
                                elif comprar<=0:
                                    print '\nOpcion no valida, presiona "enter" para continuar ... ',
                                    raw_input()
                                    repetir=1
                                    break
                                else:
                                    print '\nLo sentimos, no contamos con la cantidad de productos solicitada\n'
                                    print 'Presione "enter" para continuar ... ',
                                    raw_input()
                                    repetir=1
                                    break
                            except ValueError:
                                print '\nERROR, presiona "enter" para continuar',
                                raw_input()
                                repetir=1
                                break
                        if repetir==1 or repetir=='1':
                            ejemplo(limiteizq,limiteder,txt1)
                        break
                    else:
                        print '\nID no valido, presione "enter" para continuar ... ',
                        raw_input()
                        ejemplo(limiteizq,limiteder,txt1)
                else:
                    print '\nOpcion no valida, presiona "enter" para continuar ...',
                    raw_input()
                    ejemplo(limiteizq,limiteder,txt1)
                break
            elif sn==2:
                os.system('cls')
                infotxt()
                break
            else:
                print '\nOpcion no valida, presiona "enter" para continuar ...',
                raw_input()
                os.system('cls')
        except ValueError:
            print '\nERROR, presiona "enter" para continuar',
            raw_input()
            os.system('cls')

def infotxt():
    os.system('cls')
    menu_categorias()
    print "\n\n"
    cat1=int(raw_input("\n>> En que categoria desea buscar algun producto?: "))
    while True:
        try:
            if cat1==1:
                while True:
                    try:
                        os.system('cls')
                        menu_C1()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> En que subcategoria desea buscar algun producto?: "))
                        if subcat1==1:
                            os.system('cls')
                            txt='categoria1_1.txt'
                            ejemplo(1,5,txt)
                            break
                        elif subcat1==2:
                            while True:
                                try:
                                    os.system('cls')
                                    menu_C1_2()
                                    print "\n\n\n>> La subcategoria que selecciono se divide en mas subcategorias.\n\n",
                                    sub_subcat1=int(raw_input("   En cual desea continuar la busqueda de algun producto?: "))
                                    if sub_subcat1==1:
                                        os.system('cls')
                                        txt='categoria1_2_1.txt'
                                        ejemplo(6,10,txt)
                                        break
                                    elif sub_subcat1==2:
                                        os.system('cls')
                                        txt='categoria1_2_2.txt'
                                        ejemplo(11,13,txt)
                                        break
                                    elif sub_subcat1==3:
                                        os.system('cls')
                                        infotxt()
                                        break
                                    else:
                                        print '\nOpcion no valida, presiona "enter" para continuar',
                                        raw_input()
                                except ValueError:
                                    print '\nERROR, presiona "enter" para continuar',
                                    raw_input()
                            break
                        elif subcat1==3:
                            while True:
                                try:
                                    os.system('cls')
                                    menu_C1_3()
                                    print "\n\n\n>> La subcategoria que selecciono se divide en mas subcategorias.\n\n",
                                    sub_subcat1=int(raw_input("   En cual desea continuar la busqueda de algun producto?: "))
                                    if sub_subcat1==1:
                                        os.system('cls')
                                        txt='categoria1_3_1.txt'
                                        ejemplo(14,18,txt)
                                        break
                                    elif sub_subcat1==2:
                                        os.system('cls')
                                        txt='categoria1_3_2.txt'
                                        ejemplo(19,23,txt)
                                        break
                                    elif sub_subcat1==3:
                                        os.system('cls')
                                        infotxt()
                                        break
                                    else:
                                        print '\nOpcion no valida, presiona "enter" para continuar',
                                        raw_input()
                                except ValueError:
                                    print '\nERROR, presiona "enter" para continuar',
                                    raw_input()
                            break
                        elif subcat1==4:
                            while True:
                                try:
                                    os.system('cls')
                                    menu_C1_4()
                                    print "\n\n\n>> La subcategoria que selecciono se divide en mas subcategorias.\n\n",
                                    sub_subcat1=int(raw_input("   En cual desea continuar la busqueda de algun producto?: "))
                                    if sub_subcat1==1:
                                        os.system('cls')
                                        txt='categoria1_4_1.txt'
                                        ejemplo(24,28,txt)
                                        break
                                    elif sub_subcat1==2:
                                        os.system('cls')
                                        txt='categoria1_4_2.txt'
                                        ejemplo(29,33,txt)
                                        break
                                    elif sub_subcat1==3:
                                        os.system('cls')
                                        infotxt()
                                        break
                                    else:
                                        print '\nOpcion no valida, presiona "enter" para continuar',
                                        raw_input()
                                except ValueError:
                                    print '\nERROR, presiona "enter" para continuar',
                                    raw_input()
                            break
                        elif subcat1==5:
                            os.system('cls')
                            txt='categoria1_5.txt'
                            ejemplo(34,38,txt)
                            break
                        elif subcat1==6:
                            os.system('cls')
                            infotxt()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
            elif cat1==2:
                while True:
                    try:
                        os.system('cls')
                        menu_C2()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> En que subcategoria desea buscar algun producto?: "))
                        if subcat1==1:
                            while True:
                                try:
                                    os.system('cls')
                                    menu_C2_1()
                                    print "\n\n\n>> La subcategoria que selecciono se divide en mas subcategorias.\n\n",
                                    sub_subcat1=int(raw_input("   En cual desea continuar la busqueda de algun producto?: "))
                                    if sub_subcat1==1:
                                        os.system('cls')
                                        txt='categoria2_1_1.txt'
                                        ejemplo(39,43,txt)
                                        break
                                    elif sub_subcat1==2:
                                        os.system('cls')
                                        txt='categoria2_1_2.txt'
                                        ejemplo(44,48,txt)
                                        break
                                    elif sub_subcat1==3:
                                        os.system('cls')
                                        infotxt()
                                        break
                                    else:
                                        print '\nOpcion no valida, presiona "enter" para continuar',
                                        raw_input()
                                except ValueError:
                                    print '\nERROR, presiona "enter" para continuar',
                                    raw_input()
                            break
                        elif subcat1==2:
                            os.system('cls')
                            txt='categoria2_2.txt'
                            ejemplo(49,53,txt)
                            break
                        elif subcat1==3:
                            os.system('cls')
                            infotxt()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
                break
            elif cat1==3:
                while True:
                    try:
                        os.system('cls')
                        menu_C3()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> En que subcategoria desea buscar algun producto?: "))
                        if subcat1==1:
                            os.system('cls')
                            txt='categoria3_1.txt'
                            ejemplo(54,58,txt)
                            break
                        elif subcat1==2:
                            os.system('cls')
                            txt='categoria3_2.txt'
                            ejemplo(59,63,txt)
                            break
                        elif subcat1==3:
                            os.system('cls')
                            txt='categoria3_3.txt'
                            ejemplo(64,68,txt)
                            break
                        elif subcat1==4:
                            os.system('cls')
                            txt='categoria3_4.txt'
                            ejemplo(69,73,txt)
                            break
                        elif subcat1==5:
                            os.system('cls')
                            txt='categoria3_5.txt'
                            ejemplo(74,78,txt)
                            break
                        elif subcat1==6:
                            os.system('cls')
                            txt='categoria3_6.txt'
                            ejemplo(79,83,txt)
                            break
                        elif subcat1==7:
                            os.system('cls')
                            infotxt()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
            elif cat1==4:
                while True:
                    try:
                        os.system('cls')
                        menu_C4()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> En que subcategoria desea buscar algun producto?: "))
                        if subcat1==1:
                            os.system('cls')
                            txt='categoria4_1.txt'
                            ejemplo(84,88,txt)
                            break
                        elif subcat1==2:
                            os.system('cls')
                            txt='categoria4_2.txt'
                            ejemplo(89,93,txt)
                            break
                        elif subcat1==3:
                            os.system('cls')
                            infotxt()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
            elif cat1==5:
                os.system('cls')
                txt='categoria5.txt'
                ejemplo(94,103,txt)
                repetir=0
                break
            elif cat1==6:
                while True:
                    try:
                        os.system('cls')
                        menu_C6()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> En que subcategoria desea buscar algun producto?: "))
                        if subcat1==1:
                            os.system('cls')
                            txt='categoria6_1.txt'
                            ejemplo(104,108,txt)
                            break
                        elif subcat1==2:
                            os.system('cls')
                            txt='categoria6_2.txt'
                            ejemplo(109,113,txt)
                            break
                        elif subcat1==3:
                            os.system('cls')
                            txt='categoria6_3.txt'
                            ejemplo(114,118,txt)
                            break
                        elif subcat1==4:
                            os.system('cls')
                            txt='categoria6_4.txt'
                            ejemplo(119,123,txt)
                            break
                        elif subcat1==5:
                            while True:
                                try:
                                    os.system('cls')
                                    menu_C6_5()
                                    print "\n\n\n>> La subcategoria que selecciono se divide en mas subcategorias.\n\n",
                                    sub_subcat1=int(raw_input("   En cual desea continuar la busqueda de algun producto?: "))
                                    if sub_subcat1==1:
                                        os.system('cls')
                                        txt='categoria6_5_1.txt'
                                        ejemplo(124,128,txt)
                                        break
                                    elif sub_subcat1==2:
                                        os.system('cls')
                                        txt='categoria6_5_2.txt'
                                        ejemplo(129,133,txt)
                                        break
                                    elif sub_subcat1==3:
                                        os.system('cls')
                                        infotxt()
                                        break
                                    else:
                                        print '\nOpcion no valida, presiona "enter" para continuar',
                                        raw_input()
                                except ValueError:
                                    print '\nERROR, presiona "enter" para continuar',
                                    raw_input()
                            break
                        elif subcat1==6:
                            os.system('cls')
                            infotxt()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
            elif cat1==7:
                while True:
                    try:
                        os.system('cls')
                        menu_C7()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> En que subcategoria desea buscar algun producto?: "))
                        if subcat1==1:
                            os.system('cls')
                            txt='categoria7_1.txt'
                            ejemplo(134,138,txt)
                            break
                        elif subcat1==2:
                            os.system('cls')
                            txt='categoria7_2.txt'
                            ejemplo(139,143,txt)
                            break
                        elif subcat1==3:
                            os.system('cls')
                            txt='categoria7_3.txt'
                            ejemplo(144,148,txt)
                            break
                        elif subcat1==4:
                            os.system('cls')
                            infotxt()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
            elif cat1==8:
                while True:
                    try:
                        os.system('cls')
                        menu_C8()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> En que subcategoria desea buscar algun producto?: "))
                        if subcat1==1:
                            os.system('cls')
                            txt='categoria8_1.txt'
                            ejemplo(149,153,txt)
                            break
                        elif subcat1==2:
                            while True:
                                try:
                                    os.system('cls')
                                    menu_C8_2()
                                    print "\n\n\n>> La subcategoria que selecciono se divide en mas subcategorias.\n\n",
                                    sub_subcat1=int(raw_input("   En cual desea continuar la busqueda de algun producto?: "))
                                    if sub_subcat1==1:
                                        os.system('cls')
                                        txt='categoria8_2_1.txt'
                                        ejemplo(154,158,txt)
                                        break
                                    elif sub_subcat1==2:
                                        os.system('cls')
                                        txt='categoria8_2_2.txt'
                                        ejemplo(159,163,txt)
                                        break
                                    elif sub_subcat1==3:
                                        os.system('cls')
                                        infotxt()
                                        break
                                    else:
                                        print '\nOpcion no valida, presiona "enter" para continuar',
                                        raw_input()
                                except ValueError:
                                    print '\nERROR, presiona "enter" para continuar',
                                    raw_input()
                            break
                        elif subcat1==3:
                            os.system('cls')
                            infotxt()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
            elif cat1==9:
                while True:
                    try:
                        os.system('cls')
                        menu_C9()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> En que subcategoria desea buscar algun producto?: "))
                        if subcat1==1:
                            os.system('cls')
                            txt='categoria9_1.txt'
                            ejemplo(164,168,txt)
                            break
                        elif subcat1==2:
                            os.system('cls')
                            txt='categoria9_2.txt'
                            ejemplo(169,173,txt)
                            break
                        elif subcat1==3:
                            os.system('cls')
                            infotxt()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
            elif cat1==10: 
                while True:
                    try:
                        os.system('cls')
                        menu_ticket()
                        print "\n\n"
                        subcat1=int(raw_input("\n>> Desea guardar su ticket de compra?: "))
                        if subcat1==1:
                            shutil.copy("ticket.txt", "ticket1.txt")
                            print '\n\nTicket guardado, presione "enter" para continuar ... ',
                            raw_input()
                            os.system('cls')
                            generar_ticket()
                            cuadro()
                            break
                        elif subcat1==2:
                            os.system('cls')
                            generar_ticket()
                            cuadro()
                            break
                        else:
                            print '\nOpcion no valida, presiona "enter" para continuar ... ',
                            raw_input()
                    except ValueError:
                        print '\nERROR, presiona "enter" para continuar ... ',
                        raw_input()
                repetir=0
                break
            else:
                print '\nOpcion no valida, presiona "enter" para continuar ... ',
                raw_input()
                repetir=1
                break
        except ValueError:
            print '\nERROR, presiona "enter" para continuar ... ',
            raw_input()
            repetir=1
            break
    if repetir==1 or repetir=="1":
        os.system('cls')
        infotxt()

def datos_entrada():
    while True:
        try:
            print "\n\n"
            valor1=int(raw_input("\n>> Punto de venta. Ingrese una opcion: "))
            if valor1==1:
                user=raw_input("\n>> Ingrese su nombre de usuario: ")
                dato1="(u'"+user+"',)"
                con = sqlite3.connect('registro.s3db')
                cursor=con.cursor()
                cursor.execute("SELECT usuarios FROM users")
                for usuarios in cursor:
                    convertir1=str(usuarios)
                    if dato1==convertir1:
                        confirm1=1
                        break
                    else:
                        confirm1=0
                con.close()
                passw=raw_input("\n>> Ingrese su password: ")
                dato2="(u'"+passw+"',)"
                con = sqlite3.connect('registro.s3db')
                cursor=con.cursor()
                cursor.execute("SELECT contrasena FROM users")
                for contrasena in cursor:
                    convertir2=str(contrasena)
                    if dato2==convertir2:
                        confirm2=1
                        break
                    else:
                        confirm2=0
                con.close()
                if confirm2==1 and confirm1==1:
                    infotxt()
                else:
                    print "\n\nUsuario o password incorrectos... ",
                    raw_input()
                    os.system('cls')
                    entrar()
                repetir=0
                break
            elif valor1==2:
                os.system('cls')
                repetir=0
                cuadro()
                break
            else:
                print '\nOpcion no valida, presiona "enter" para continuar',
                raw_input()
                repetir=1
                break
        except ValueError:
            print '\nERROR, presiona "enter" para continuar',
            raw_input()
            repetir=1
            break
    if repetir==1 or repetir=="1":
        os.system("cls")
        entrar()

def datos_registro():
    while True:
        try:
            print "\n\n"
            valor1=int(raw_input("\n>> Punto de venta. Ingrese una opcion: "))
            if valor1==1:
                user=raw_input("\n>> Ingrese un nombre de usuario (8 digitos): ")
                passw=raw_input("\n>> Ingrese un password (8 digitos): ")
                if len(user)==8 and len(passw)==8:
                    con = sqlite3.connect('registro.s3db')
                    cursor = con.cursor()
                    cursor.execute("insert into users(usuarios, contrasena) values('"+user+"','"+passw+"')")
                    con.commit()
                    con.close()
                    print '\n\nDATOS GUARDADOS. Presiona "Enter" para continuar ... ',
                    raw_input()
                    os.system('cls')
                    repetir=0
                    cuadro()
                    break
                else:
                    print u'\n>> ERROR, Usuario y/o contraseña deben tener 8 dígitos. Presiona "Enter" para continuar ... ',
                    raw_input()
                    repetir=1
                    break
            elif valor1==2:
                os.system('cls')
                repetir=0
                cuadro()
                break
            else:
                print '\nOpcion no valida, presiona "enter" para continuar',
                raw_input()
                repetir=1
                break
        except ValueError:
            print '\nERROR, presiona "enter" para continuar',
            raw_input()
            repetir=1
            break
    if repetir==1 or repetir=="1":
        os.system("cls")
        registro()

def acerca():
    i=1
    sep1="                                "
    print "\n"+sep1,
    for i in range(61):
        print "*",
    f = open ('acercade.txt','r')
    mensaje = f.read()
    print mensaje
    f.close()
    print sep1,
    for i in range(61):
        print "*",
    print u'\n\n\n\n\nPresione "ENTER" para regresar al Menú Principal ... ',
    raw_input()
    os.system("cls")
    cuadro()

def entrar():
    menu_sesion()
    datos_entrada()

def registro():
    menu_registro()
    datos_registro()

def opciones():
    while True:
        try:
            print "\n\n"
            valor1=int(raw_input("\n>> Punto de venta. Ingrese una opcion: "))
            if valor1==1:
                os.system('cls')
                entrar()
                repetir=0
                break
            elif valor1==2:
                os.system('cls')
                registro()
                repetir=0
                break
            elif valor1==3:
                os.system('cls')
                acerca()
                repetir=0
                break
            elif valor1==4:
                os.system('cls')
                return
                break
            else:
                print '\nOpcion no valida, presiona "enter" para continuar',
                raw_input()
                repetir=1
                break
        except ValueError:
            print '\nERROR, presiona "enter" para continuar',
            raw_input()
            repetir=1
            break
    if repetir==1 or repetir=="1":
        os.system("cls")
        cuadro()

def cuadro():
    menu_principal()
    opciones()

os.system('cls')
cuadro()
