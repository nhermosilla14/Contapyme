# -*- coding: utf-8 -*-
#
#  backend.py
#  
#  Funciones para modificar las bases de datos con independencia  
#  de la interfaz utilizada.
#
#  Copyright 2015-2016 Nicolás Hermosilla P. <nhermosilla14@gmail.com>
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

import os
from datetime import datetime
COMPAT = 0 # Modo de compatibilidad

# Elimina la línea deseada del archivo indicado. La primera es la 0.
def eliminar_linea(archivo,linea):
    a = open(archivo)
    tmp = open(".tmp","w")
    indice = 0
    for l in a:
        if indice != linea:
                tmp.write(l)
        indice += 1
    tmp.close()
    a.close()
    os.renames(".tmp",archivo)

# Devuelve lista de la forma:
# [('Bebidas','Todo tipo de bebestibles','bebidas.dat'),('Chocolates','Trencitos, Sahne Nuss, Capri, etc','chocolates.dat')]
def obtener_tipos():
    arch_tipos = open("data/tipos.dat","r")
    tipos = list()
    for linea in arch_tipos:
        datos = tuple(linea.split(";"))
        tipos.append(datos)
    # Está lista la tupla con los tipos de productos!
    arch_tipos.close()
    return tipos
    
# Lee el archivo del tipo de producto y retorna una lista de tuplas,
# de la forma [(Ginger Ale,10,700,300,2,2015/02/01),(Papaya,5,700,300,4,2015/02/03),
# (Nombre,inventario,valor,ganancia,venta_actual,fecha_última_venta)]
def obtener_productos(nombre):
    # Modo de compatibilidad
    if COMPAT == 1:
            detectar_antiguo(nombre)
    arch_elegido = open("data/"+nombre)
    #if len(arch_elegido.readline().split(',')) == 4:
    #       arch_elegido.close()
    #       migrar_dat(nombre)
    #       arch_elegido = open("data/"+nombre)
    productos = list()
    for linea in arch_elegido:
        datos = tuple(linea.split(","))
       # Ginger Ale,10,700,300,2,4,2,2015/02/01
        productos.append(datos)
    # Listo el listado de tuplas con el tipo elegido
    arch_elegido.close()
    return productos

# Resta la 'cantidad' de 'producto' del 'archivo'
# Se utiliza principalmente para reducir el inventario en la función
# ingresar_venta, y para aumentarlo en ingresar_compra.
# Desde la versión 1.2, también se encarga de actualizar el número de
# ventas del día, además de la venta promedio y la fecha de última venta.
# Para la versión 1.3, falta reemplazar el método de cálculo de la venta promedio,
# así como el formato de la base de datos, por una que almacene más datos, y de
# manera más precisa.

# Desde la versión 2.0 se descontinuan los datos de venta del día y ventas promedio

def actualizar_inventario(cantidad,producto,archivo,tipo='venta'):
    datos = open("data/"+archivo)
    tmp = open("data/.tmp","w")
    #if len(datos.readline().split(',')) == 4:
    #       datos.close()
    #       migrar_dat(archivo)
    #       datos = open("data/"+archivo)
    for linea in datos:
        if linea.split(',')[0] == producto and tipo == 'venta':
            inventario = str(int(linea.split(',')[1])-cantidad)
            precio_venta = linea.split(',')[2]
            ganancia = linea.split(',')[3]
            venta_dia = linea.split(',')[4]                        
            #venta_prom = linea.split(',')[5]
            #dias_a_la_venta = linea.split(',')[6]
            ultima_venta = linea.split(',')[5].strip()
            if ultima_venta != str(datetime.now().year)+'/'+str(datetime.now().month)+'/'+str(datetime.now().day):
                ultima_venta = str(datetime.now().year)+'/'+str(datetime.now().month)+'/'+str(datetime.now().day)
          #      #dias_a_la_venta = str(int(dias_a_la_venta)+1)
                venta_dia = '0'
            venta_dia = str(int(venta_dia)+cantidad)
          #  #venta_prom = str(round((int(venta_prom)*(int(dias_a_la_venta)-1)+int(venta_dia))/int(dias_a_la_venta)))
            tmp.write(producto+','+inventario+','+precio_venta+','+ganancia+','+venta_dia+','+ultima_venta+'\n')
        elif linea.split(',')[0] == producto and tipo == 'compra':
            inventario = str(int(linea.split(',')[1])-cantidad)
            precio_venta = linea.split(',')[2]
            ganancia = linea.split(',')[3]
            venta_dia = linea.split(',')[4]
            #venta_prom = linea.split(',')[5]
            #dias_a_la_venta = linea.split(',')[6]
            ultima_venta = linea.split(',')[5].strip()
            tmp.write(producto+','+inventario+','+precio_venta+','+ganancia+','+venta_dia+','+ultima_venta+'\n')
        else:
            tmp.write(linea)
    datos.close()
    tmp.close()
    os.renames("data/.tmp","data/"+archivo) 

# Suma a los balances la cantidad bruta y líquida
def actualizar_balances(bruto,liquido):
    encontrada = 0
    fecha = str(datetime.now().year)+','+str(datetime.now().month)+','+str(datetime.now().day)
    try:
        datos = open("data/balances.dat")
    except:
        open("data/balances.dat",'a').close()
        datos = open("data/balances.dat")
    tmp = open("data/.tmp","w")
    for linea in datos:
        if linea.split(';')[0] == fecha:
            tmp.write(fecha+';'+str(int(linea.split(';')[1].split(',')[0])+bruto)+','+str(int(linea.split(';')[1].split(',')[1])+liquido)+'\n')
            encontrada = 1
        else:
            tmp.write(linea)
    tmp.close()
    datos.close()
    os.renames("data/.tmp","data/balances.dat")
    if encontrada == 0:
        datos = open("data/balances.dat","a")
        datos.write(fecha+';'+str(bruto)+','+str(liquido)+'\n')
        datos.close()

#Función hecha para reemplazar y unificar las operaciones de compra y venta.
# Recibe los siguientes argumentos:
# productos: lista de tuplas con los productos, retornada por obtener_productos
# nombre: nombre del archivo de base de datos correspondiente
# tipo: tipo de transacción. 1 es venta, 0 es compra.
# cantidad: número de unidades a transar.
# indice: indice del producto elegido para ubicarlo en la lista.
def operar_transaccion(productos,nombre,tipo,cantidad,indice):
    # Venta
    if tipo == 1:
        actualizar_inventario(cantidad,productos[indice][0],nombre)
        bruto = cantidad*int(productos[indice][2])
        liquido = cantidad*int(productos[indice][3])
        return bruto,liquido
    # Compra
    elif tipo == 0:
        actualizar_inventario(-1*cantidad,productos[indice][0],nombre,'compra')

# Detecta archivos de configuración antiguos, y los migra al nuevo formato.
# El formato de 8 partes, versión 1.2, posee numerosos bugs. Es necesario migrar
# las bases de datos a un formato nuevo.

# Descontinuado desde versión 2.0
def detectar_antiguo(archivo):
    datos = open("data/"+archivo)
    if len(datos.readline().split(',')) == 4:
        datos.close()
        migrar_dat(archivo)
    else:
        datos.close() 

# Función para migrar archivos de base de datos antigua al nuevo formato.
# Necesita actualizarse para entregar soporte para un formato mejorado.

# Descontinuado desde versión 2.0
def migrar_dat(archivo):
    dat = open("data/"+archivo,'r')
    tmp = open("data/.tmp",'w')
    for linea in dat:
        tmp.write(linea.strip()+','+'0'+','+'0'+','+'0'+','+'2000/1/1'+'\n')
    dat.close()
    tmp.close()
    os.renames('data/.tmp','data/'+archivo)

def agregar_producto(producto,categoria):
    archivo = open("data/"+categoria,"r")
    presente = False
    for linea in archivo:
        if producto[0] in linea.split(','):
            presente = True
            print(presente)
            break
    archivo.close()
    if not presente:
        archivo = open("data/"+categoria,"a")
        linea = producto[0]+','+producto[1]+','+producto[2]+','+producto[3]+','+'0'+','+'2000/1/1'+'\n'
        archivo.write(linea)
        archivo.close()
        return 0
    else:
        return 1

