#!/usr/bin/env python
# -*- coding: utf-8 -*-

def menu_principal():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                               UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO                               "+c
    for i in range(3):
        print sep2+c+sep3+c
    print sep2+c+u"                                       Facultad de Ingeniería                                        "+c
    for i in range(3):
        print sep2+c+sep3+c
    print sep2+c+u"                                    División de Ciencias Básicas                                     "+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                       §§ PROYECTO. COMPUTEC §§                                      "+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                         (1) Iniciar sesion                                          "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                           (2) Registrarme                                           "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                            (3) Acerca de                                            "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                              (4) Salir                                              "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_sesion():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                            ¤          ¤                                             "+c
    print sep2+c+u"                                          ¤              ¤                                           "+c
    print sep2+c+u"                                   ■■■■ ¤       ■■■■       ¤ ■■■■                                    "+c
    print sep2+c+u"                                      ¤       ▀     ▀        ¤                                       "+c
    print sep2+c+u"                              ██████ ¤        █               ¤ ██████                               "+c
    print sep2+c+u"                                      ¤       ▄     ▄        ¤                                       "+c
    print sep2+c+u"                                   ■■■■ ¤       ■■■■       ¤ ■■■■                                    "+c
    print sep2+c+u"                                          ¤              ¤                                           "+c
    print sep2+c+u"                                            ¤          ¤                                             "+c
    for i in range(3):
        print sep2+c+sep3+c
    print sep2+c+u"                            ▄▀▀▀ ▄▀▀▀▄ █▀▄ ▄▀█ █▀▀█ █  █ ▀▀█▀▀ █▀▀▀ ▄▀▀▀                             "+c
    print sep2+c+u"                            █    █   █ █  ▀  █ █▀▀▀ █  █   █   █▀▀  █                                "+c
    print sep2+c+u"                             ▀▀▀  ▀▀▀  ▀     ▀ ▀    ▀▀▀▀   ▀   ▀▀▀▀  ▀▀▀                             "+c
    for i in range(6):
        print sep2+c+sep3+c
    print sep2+c+u"                                      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█                                       "+c
    print sep2+c+u"                                      █ (1)  INICIAR SESIÓN  █                                       "+c
    print sep2+c+u"                                      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█                                       "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█                                       "+c
    print sep2+c+u"                                      █  (2)  MENÚ PRICIPAL  █                                       "+c
    print sep2+c+u"                                      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█                                       "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_registro():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                            ¤          ¤                                             "+c
    print sep2+c+u"                                          ¤              ¤                                           "+c
    print sep2+c+u"                                   ■■■■ ¤       ■■■■       ¤ ■■■■                                    "+c
    print sep2+c+u"                                      ¤       ▀     ▀        ¤                                       "+c
    print sep2+c+u"                              ██████ ¤        █               ¤ ██████                               "+c
    print sep2+c+u"                                      ¤       ▄     ▄        ¤                                       "+c
    print sep2+c+u"                                   ■■■■ ¤       ■■■■       ¤ ■■■■                                    "+c
    print sep2+c+u"                                          ¤              ¤                                           "+c
    print sep2+c+u"                                            ¤          ¤                                             "+c
    for i in range(3):
        print sep2+c+sep3+c
    print sep2+c+u"                            ▄▀▀▀ ▄▀▀▀▄ █▀▄ ▄▀█ █▀▀█ █  █ ▀▀█▀▀ █▀▀▀ ▄▀▀▀                             "+c
    print sep2+c+u"                            █    █   █ █  ▀  █ █▀▀▀ █  █   █   █▀▀  █                                "+c
    print sep2+c+u"                             ▀▀▀  ▀▀▀  ▀     ▀ ▀    ▀▀▀▀   ▀   ▀▀▀▀  ▀▀▀                             "+c
    for i in range(6):
        print sep2+c+sep3+c
    print sep2+c+u"                                      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█                                       "+c
    print sep2+c+u"                                      █    (1)  REGISTRO     █                                       "+c
    print sep2+c+u"                                      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█                                       "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█                                       "+c
    print sep2+c+u"                                      █  (2)  MENÚ PRICIPAL  █                                       "+c
    print sep2+c+u"                                      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█                                       "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_categorias():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                        Bienvenido ",
    print "holaaaaa"+"                                         "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> CATEGORÍAS <<                                            "+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"          (1) -> CÓMPUTO (Hardware)                              (2) -> IMPRESIÓN Y COPIADO          "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (3) -> COMPUTADORAS                                    (4) -> WEBCAM Y AUDIO               "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (5) -> ENERGÍA                                         (6) -> SOFTWARE                     "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (7) -> APPLE                                           (8) -> TELECOMUNICACIONES           "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (9) -> AUDIO Y VIDEO                                                                       "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                      (10) -> CERRAR SESIÓN                                          "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_opciones():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="  "
    sep3="                                                             "
    print "\n"+" ",
    for i in range(32):
        print c,
    print "\n",
    for i in range(3):
        print sep2+c+sep3+c
    print sep2+c+u"                           OPCIONES                          "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"        (1) -> Comprar                 (2) -> Regresar       "+c
    for i in range(3):
        print sep2+c+sep3+c
    print " ",
    for i in range(32):
        print c,

def menu_ticket():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                              OPCIONES                                               "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                       >> TICKET DE COMPRA <<                                        "+c
    for i in range(7):
        print sep2+c+sep3+c
    print sep2+c+u"                   (1) -> GUARDAR                                  (2) -> BORRAR                     "+c
    for i in range(17):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_C1():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                    CATEGORÍA. CÓMPUTO (HARDWARE)                                    "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> SUBCATEGORÍAS <<                                         "+c
    for i in range(6):
        print sep2+c+sep3+c
    print sep2+c+u"          (1) -> TARJETAS MADRE                                 (2) -> TARJETAS DE VIDEO             "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (3) -> DISPOSITIVOS DE ENTRADA                        (4) -> DISCOS DUROS                  "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (5) -> PROCESADORES                                                                        "+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (6) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_C1_2():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                    CATEGORÍA. CÓMPUTO (HARDWARE)                                    "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                   SUBCATEGORÍA. TARJETAS DE VIDEO                                   "+c
    print sep2+c+sep3+c
    print sep2+c+sep3+c
    print sep2+c+u"                                       >> SUB-SUBCATEGORÍAS <<                                       "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"           (1) -> USO EXTREMO                                         (2) -> USO ESENCIAL            "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (3) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_C1_3():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                    CATEGORÍA. CÓMPUTO (HARDWARE)                                    "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                SUBCATEGORÍA. DISPOSITIVOS DE ENTRADA                                "+c
    print sep2+c+sep3+c
    print sep2+c+sep3+c
    print sep2+c+u"                                       >> SUB-SUBCATEGORÍAS <<                                       "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"           (1) -> TECLADOS                                                  (2) -> MOUSE             "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (3) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_C1_4():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                    CATEGORÍA. CÓMPUTO (HARDWARE)                                    "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                     SUBCATEGORÍA. DISCOS DUROS                                      "+c
    print sep2+c+sep3+c
    print sep2+c+sep3+c
    print sep2+c+u"                                       >> SUB-SUBCATEGORÍAS <<                                       "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"           (1) -> DISCOS DUROS INTERNOS                     (2) -> DISCOS DUROS INTERNOS             "+c
    print sep2+c+u"                      PARA PC                                          PARA LAPTOP                   "+c
    for i in range(7):
        print sep2+c+sep3+c
    print sep2+c+u"                                          (3) -> REGRESAR                                            "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_C2():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                    CATEGORÍA. IMPESIÓN Y COPIADO                                    "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> SUBCATEGORÍAS <<                                         "+c
    for i in range(7):
        print sep2+c+sep3+c
    print sep2+c+u"               (1) -> IMPRESORAS Y                                  (2) -> ESCÁNERS                  "+c
    print sep2+c+u"                    MULTIFUNCIONALES                                                                 "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (3) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_C2_1():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                    CATEGORÍA. IMPRESIÓN Y COPIADO                                   "+c
    print sep2+c+sep3+c
    print sep2+c+u"                             SUBCATEGORÍA. IMPRESORAS Y MULTIFUNCIONALES                             "+c
    print sep2+c+sep3+c
    print sep2+c+sep3+c
    print sep2+c+u"                                       >> SUB-SUBCATEGORÍAS <<                                       "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"            (1) -> IMPRESORAS A COLOR                       (2) -> IMPRESORAS A BLANCO Y NEGRO       "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (3) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_C3():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                       CATEGORÍA. COMPUTADORAS                                       "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> SUBCATEGORÍAS <<                                         "+c
    for i in range(6):
        print sep2+c+sep3+c
    print sep2+c+u"          (1) -> PC DE ESCRITORIO                                  (2) -> LAPTOPS                    "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (3) -> TABLETAS                                          (4) -> ALL IN ONE                 "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (5) -> WORKSTATIONS                                      (6) -> ACCESORIOS PARA PC         "+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (7) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_C4():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                      CATEGORÍA. WEBCAM & AUDIO                                      "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> SUBCATEGORÍAS <<                                         "+c
    for i in range(7):
        print sep2+c+sep3+c
    print sep2+c+u"                   (1) -> WEBCAM                                  (2) -> AUDÍFONOS                   "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"                                          (3) -> REGRESAR                                            "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_C6():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                         CATEGORÍA. SOFTWARE                                         "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> SUBCATEGORÍAS <<                                         "+c
    for i in range(6):
        print sep2+c+sep3+c
    print sep2+c+u"          (1) -> SISTEMAS OPERATIVOS                            (2) -> OFFICE                        "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (3) -> ANTIVIRUS                                      (4) -> DISEÑO Y MULTIMEDIA           "+c
    print sep2+c+sep3+c
    print sep2+c+u"          (5) -> VIDEOJUEGOS                                                                         "+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (6) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_C6_5():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                         CATEGORÍA. SOFTWARE                                         "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                      SUBCATEGORÍA. VIDEOJUEGOS                                      "+c
    print sep2+c+sep3+c
    print sep2+c+sep3+c
    print sep2+c+u"                                       >> SUB-SUBCATEGORÍAS <<                                       "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"          (1) -> VIDEOJUEGOS XBOX ONE                           (2) -> VIDEOJUEGOS XBOX 360          "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (3) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_C7():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                          CATEGORÍA. APPLE                                           "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> SUBCATEGORÍAS <<                                         "+c
    for i in range(7):
        print sep2+c+sep3+c
    print sep2+c+u"                  (1) -> IPADS                                        (2) -> IPODS                   "+c
    print sep2+c+sep3+c
    print sep2+c+u"                  (3) -> MACBOOKS                                                                    "+c
    for i in range(7):
        print sep2+c+sep3+c
    print sep2+c+u"                                          (4) -> REGRESAR                                            "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_C8():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                    CATEGORÍA. TELECOMUNICACIONES                                    "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> SUBCATEGORÍAS <<                                         "+c
    for i in range(7):
        print sep2+c+sep3+c
    print sep2+c+u"             (1) -> TELEFONÍA MÓVIL                             (2) -> TELEFONÍA CONVENCIONAL        "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"                                          (3) -> REGRESAR                                            "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,

def menu_C8_2():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                    CATEGORÍA. TELECOMUNICACIONES                                    "+c
    print sep2+c+sep3+c
    print sep2+c+u"                                 SUBCATEGORÍA. TELEFONÍA CONVENCIONAL                                "+c
    print sep2+c+sep3+c
    print sep2+c+sep3+c
    print sep2+c+u"                                       >> SUB-SUBCATEGORÍAS <<                                       "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"         (1) -> TELÉFONOS ALÁMBRICOS                            (2) -> TELÉFONOS INALÁMBRICOS        "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep2+c+u"                                           (3) -> REGRESAR                                           "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,


def menu_C9():
    c=u'¤'
    i=1
    sep1="                                           "
    sep2="                                            "
    sep3="                                                                                                     "
    print "\n"+sep1,
    for i in range(52):
        print c,
    print "\n"+sep2+c+sep3+c
    for i in range(5):
        print sep2+c+sep3+c
    print sep2+c+u"                                      CATEGORÍA. AUDIO & VIDEO                                       "+c
    for i in range(4):
        print sep2+c+sep3+c
    print sep2+c+u"                                         >> SUBCATEGORÍAS <<                                         "+c
    for i in range(7):
        print sep2+c+sep3+c
    print sep2+c+u"                 (1) -> PANTALLAS                                  (2) -> CONSOLAS                   "+c
    for i in range(9):
        print sep2+c+sep3+c
    print sep2+c+u"                                          (3) -> REGRESAR                                            "+c
    for i in range(8):
        print sep2+c+sep3+c
    print sep1,
    for i in range(52):
        print c,
