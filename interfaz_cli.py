# -*- coding: utf-8 -*-
#
#  principales.py
#  
#  Copyright 2015 Nicolás Hermosilla P. <nhermosilla14@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from backend import *

colors = {'PURPLE' : '\033[95m','BLUE' : '\033[94m'
    ,'GREEN' : '\033[92m','YELLOW' : '\033[93m'
    ,'RED' : '\033[91m','ENDC' : '\033[0m'
    ,'BOLD' : '\033[1m','UNDERLINE' : '\033[4m'
    ,'PURPLE_BOLD' : '\033[95m\033[1m'
    ,'BLUE_BOLD' : '\033[94m\033[1m'
    ,'GREEN_BOLD' : '\033[92m\033[1m'
    ,'YELLOW_BOLD' : '\033[93m\033[1m'
    ,'RED_BOLD' : '\033[91m\033[1m'}

def print_color(mensaje,color):
    print(colors[color]+mensaje+colors['ENDC'])

def bienvenida():
    print('===========================================================================================================')
    print('===========================================================================================================')
    print('==                                                                                                       ==')
    print('==                                          C O N T A P Y M E                                            ==')
    print('==                                                                                                       ==')
    print('==                               Programa de Contabilidad Fácil para Pymes                               ==')
    print('==                                                                                                       ==')
    print('==                         (c) 2015-2016 Nicolás Hermosilla - nhermosilla14@gmail.com                    ==')
    print('==                                                                                                       ==')
    print('==                                            Versión 2.0                                                ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                   Presiona ENTER para continuar...                                    ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('===========================================================================================================')
    print('===========================================================================================================')
    #actualizar_dat()
    input()
    
    
def menu_principal():
    os.system('clear')
    print('===========================================================================================================')
    print('===========================================================================================================')
    print('==                                                                                                       ==')
    print('==                                         ¿Qué deseas hacer?                                            ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                         1. Ingresar venta.                                            ==')
    print('==                                         2. Ingresar compra.                                           ==')
    print('==                                         3. Editar base de datos.                                      ==')
    print('==                                         4. Ver balances.                                              ==')
    print('==                                         5. Ver stock.                                                 ==')
    print('==                                         6. Salir.                                                     ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('===========================================================================================================')
    opc = input("==>> ")
    return opc
    
def menu_db():
    os.system('clear')
    print('===========================================================================================================')
    print('===========================================================================================================')
    print('==                                                                                                       ==')
    print('==                                         ¿Qué deseas hacer?                                            ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                         1. Ingresar producto.                                         ==')
    print('==                                         2. Eliminar producto.                                         ==')
    print('==                                         3. Ingresar categoría.                                        ==')
    print('==                                         4. Eliminar categoría.                                        ==')
    print('==                                         5. Volver al menú principal.                                  ==')
    print('==                                         6. Salir.                                                     ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('==                                                                                                       ==')
    print('===========================================================================================================')
    opc = input("==>> ")
    return opc


# Devuelve el índice del tipo elegido
def mostrar_tipos(tipos,modificador=0):
    os.system('clear')
    indice = 0
    opc = '-1'
    if modificador == 0:
        print_color("Selecciona el tipo de producto (sólo el número) para ver el stock disponible, o ingresa 0 para volver al menú anterior: \n\n","YELLOW")
    else:
        print("Los tipos de producto actuales son los siguientes:\n\n")
    for tipo in tipos:
        indice = indice + 1
        linea = str(indice)+". "
        linea = linea + tipo[0] + ": " + tipo[1]
        print(linea.replace(',,',';'))
    print("")
    if modificador == 0:
        eleccion_valida = False
        while eleccion_valida == False:
            try:
                opc = input("==>>")
                while ( opc == '' or int(opc) < 0 or int(opc) > indice ):
                    print("Ingrese una opción válida")
                    opc = input("==>> ")
                elegido = int(opc)-1
                eleccion_valida = True
            except:
                print("Ingrese una opción válida")
        os.system('clear')
        return elegido
    else:
        return 0

# Muestra el stock disponible del tipo seleccionado. Si se usa el modificador,
# se puede pedir al usuario que elija alguno de la lista.
def mostrar_stock(productos,nombre,modificador=0):
    indice = 0
    opc = '-1'
    if modificador != 0:
        print('Selecciona el producto (sólo el número), o ingresa 0 para volver al menú anterior:\n\n')
    print("   Producto".ljust(25)+"Quedan".center(8)+" Valen".center(8)+"Venta Hoy".center(12)+"Última Venta".center(15)+'\n')
    for cada in productos:
        indice = indice + 1
        linea = str(indice)+". "
        linea = linea + cada[0]
        linea = linea.ljust(25)
        linea += cada[1].center(8)+('$'+cada[2]).center(8)
        linea += cada[4].center(14)
        #linea += cada[5].center(12)
        if cada[5].strip() == '2000/1/1':
            linea += '-'.center(15)
        else: 
            linea += (cada[5].split('/')[2].strip()+'/'+cada[5].split('/')[1]+'/'+cada[5].split('/')[0]).center(15)
        print(linea)
    if modificador == 0:
        return 0
    else:
        eleccion_valida = False
        while eleccion_valida == False:
            try:
                opc = input("==>>")
                while ( opc == '' or int(opc) < 0 or int(opc) > indice ):
                    print("Ingrese una opción válida")
                    opc = input("\n==>> ")
                elegido = int(opc)-1
                eleccion_valida = True
            except:
                print("Ingrese una opción válida.")
        return elegido

# 
# Funciones principales
#
########################################################################
def ingresar_transaccion(tipo):
    # Determinar tipos  
    tipos = obtener_tipos()
    # Imprimir menú y solicitar tipo
    while True:
        elegido = mostrar_tipos(tipos)
        os.system('clear')
        if elegido == -1:
            break
        print(tipos[elegido][0]+": "+tipos[elegido][1]+'\n\n')
        nombre = tipos[elegido][2].strip()
        while True:
            os.system('clear')
            productos = obtener_productos(nombre)
            indice = mostrar_stock(productos,nombre,1)
            if indice < -1 or indice > len(productos)-1:
                continue
            if indice == -1:
                break
            listo = False
            while not listo:
                try:
                    cantidad = int(input("\nCantidad: "))
                    listo = True
                except:
                    pass
            if tipo == 'venta':
                bruto,liquido = operar_transaccion(productos,nombre,1,cantidad,indice)
                # Se tiene el monto líquido y bruto
                actualizar_balances(bruto,liquido)
            else:
                operar_transaccion(productos,nombre,0,cantidad,indice)

def ver_balances():
    os.system('clear')
    balances = open("data/balances.dat")
    cabecera = "Fecha".ljust(12)+"Ingresos brutos".ljust(17)+"Ingresos líquidos\n"
    print(cabecera)
    for linea in balances:
        l = linea.split(';')[0].split(',')[2]+'/'+linea.split(';')[0].split(',')[1]+'/'+linea.split(';')[0].split(',')[0]
        l = l.ljust(12)
        l = l + ('$'+linea.split(';')[1].split(',')[0].strip()).ljust(17)
        l = l + ('$'+linea.split(';')[1].split(',')[1].strip()).ljust(17)
        print(l)
    print('\n\n')
    input("Presiona ENTER para volver al menú principal...")

def ver_stock():
    # Determinar tipos  
    tipos = obtener_tipos()
    # Imprimir menú y solicitar tipo
    while True:
        elegido = mostrar_tipos(tipos)
        if elegido == -1:
            break
        os.system('clear')
        print(tipos[elegido][0]+": "+tipos[elegido][1]+'\n\n')
        nombre = tipos[elegido][2].strip()
        productos = obtener_productos(nombre)
        mostrar_stock(productos,nombre)
        input("\n\nPresiona ENTER para volver al menú anterior...")

def ingresar_producto():
    # Determinar tipos  
    tipos = obtener_tipos()
    # Imprimir menú y solicitar tipo
    elegido = mostrar_tipos(tipos)
    if elegido == -1:
        return
    os.system('clear')
    print(tipos[elegido][0]+": "+tipos[elegido][1]+'\n\n')
    categoria = tipos[elegido][2].strip()
    resultado = 1
    while resultado == 1:
        producto = input("Ingresa el nombre del producto (por ej: Ginger Ale), o ingresa 0 para volver atrás: ")
        if producto == '0':
            break
        stock = input("Ingresa la cantidad en stock (puede ser 0): ")
        venta = input("Ingresa el precio de venta: $")
        margen = input("Ingresa la utilidad obtenida por cada venta: $")
        datos_a_ingresar = (producto,stock,venta,margen)
        resultado = agregar_producto(datos_a_ingresar,categoria)
        if resultado == 1:
            os.system("clear")
            print("El producto ya existe. Intenta nuevamente.\n\n")
    
def eliminar_producto():
    # Determinar tipos  
    tipos = obtener_tipos()
    # Imprimir menú y solicitar tipo
    elegido = mostrar_tipos(tipos)
    os.system('clear')
    print(tipos[elegido][0]+": "+tipos[elegido][1]+'\n\n')
    nombre = tipos[elegido][2].strip()
    productos = obtener_productos(nombre)
    l = mostrar_stock(productos,nombre,1)
    eliminar_linea("data/"+nombre,l)

def ingresar_categoria():
    db = open("data/tipos.dat","a")
    tipos = obtener_tipos()
    mostrar_tipos(tipos,1)
    nombre = input("\n\nIngrese nuevo tipo (por ej: Bebidas): ")
    descripcion = (input("Ingrese descripción (por ej: Todo tipo de bebestibles): ")).replace(";",",,")
    ubicacion = input("Ingrese nombre de archivo de base de datos (por ej: bebidas.dat): ")
    linea = nombre+';'+descripcion+';'+ubicacion+'\n'
    db.write(linea)
    db.close()
    db = open("data/"+ubicacion,"w")
    db.close()

def eliminar_categoria():
    db = open("data/tipos.dat","r")
    tipos = obtener_tipos()
    mostrar_tipos(tipos,1)
    elegido = int(input("\n\nSeleccione la categoría a eliminar (sólo el número): "))-1
    indice = 0
    for linea in db:
        if indice == elegido:
            archivo = "data/"+linea.split(';')[2].strip()
            break
        indice += 1
    db.close()
    eliminar_linea("data/tipos.dat",elegido)
    os.remove(archivo)
    return None

def editar_db():
    resp = menu_db()
    while (resp != '5'):
        if resp == '1':
            ingresar_producto()
        elif resp == '2':
            eliminar_producto()
        elif resp == '3':
            ingresar_categoria()
        elif resp == '4':
            eliminar_categoria()
        elif resp == '6':
            exit()
        resp = menu_db()
