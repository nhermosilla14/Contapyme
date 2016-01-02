#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Contapyme.py
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

from interfaz_cli import *

def main():
        os.system('clear')
        bienvenida()
        resp = menu_principal()
        while (resp != '6'):
                if resp == '1':
                        ingresar_transaccion('venta')
                elif resp == '2':
                        ingresar_transaccion('compra')
                elif resp == '3':
                        editar_db()
                elif resp == '4':
                        ver_balances()
                elif resp == '5':
                        ver_stock()
                resp = menu_principal()
        os.system('clear')
        return 0


if __name__ == '__main__':
        main()

