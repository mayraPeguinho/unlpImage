import os
import sys

import PySimpleGUI as sg

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funcionalidad import constantes
from funcionalidad import actualizar_datos as act
from pantallas import nuevo_perfil
from pantallas import menu_principal
import rutas as r

def mostrar_perfiles(datos):
    '''Esta funcion carga los diferentes perfiles creados previamente
       en diferentes botones que seran mostrados luego en la ventana de inicio.
       "datos" se trata de una lista de diccionarios con la informacion de los
       usuarios. Retorna la variable perfiles que contiene los botones para cada
       usuario en la aplicacion.
    '''
    perfiles=[]
    for numero,elemento in enumerate(datos): 
        imagen_bytes=act.mostrar_imagen(os.path.join(r.ruta_imagenes_perfil,elemento["Avatar"]))
        perfiles.append(sg.Column([[sg.Button(image_data=imagen_bytes,
                                              key=numero)],
                                   [sg.Text(elemento["Usuario"])]
                                  ])
                        )
    return perfiles

def layout_inicio(datos,no_desplegar=True):
    '''Esta funcion retorna el layout de la ventana de inicio
       dependiendo de cuantos perfiles cargados haya previamente.
       "datos" es la lista de diccionarios sacada del json de perfiles
       y "no_desplegar" el booleano para indicar que tipo de layout se desea
    '''
    perfiles=mostrar_perfiles(datos)
    if(perfiles==[]):
         layout=[[sg.Button("+",key="-AGREGAR PERFIL-")]]
    elif(perfiles.__len__() <= constantes.CANTIDAD_PERFILES):
        perfiles.append(sg.Button("+",key="-AGREGAR PERFIL-"))
        layout=[[perfiles]]
    elif (constantes.CANTIDAD_PERFILES < perfiles.__len__()) and no_desplegar:
        layout = [[perfiles[0],perfiles[1],perfiles[2],perfiles[3],sg.Button("+",key="-AGREGAR PERFIL-")],
                  [sg.Button("Ver más",key="-VER MAS-")]]
    elif (constantes.CANTIDAD_PERFILES < perfiles.__len__()) and not(no_desplegar):
        perfiles.append(sg.Button("+",key="-AGREGAR PERFIL-"))
        layout = [[perfiles],
                  [sg.Button("Ver menos",key="-VER MENOS-")]]
    return layout

def mostrar_mas_perfiles(datos):
    '''Esta funcion retorna la ventana en donde se muestran los perfiles restantes'''
    layout=layout_inicio(datos,False)
    return sg.Window("Inicio",layout,margins=(200, 150))

def generar_ventana_de_inicio(datos):
    '''Esta funcion retorna una pantalla con un maximo de cuatro perfiles,
    que pasada esa cantidad estará hablitado el boton "Ver mas"
    para ver los restantes perfiles creados'''
    layout=layout_inicio(datos,True)
    return sg.Window("Inicio",layout,margins=(200, 150))

def manejar_eventos_mas_perfiles(datos,keys):
    '''Maneja los eventos de la ventana que muestra todos los perfiles.
    "keys" se trata una lista con las llaves de los botones de los perfiles'''
    mas_perfiles=mostrar_mas_perfiles(datos)
    while True:
        evento, valores = mas_perfiles.read()
        match evento:
            case sg.WIN_CLOSED:
                sys.exit()
            case "-VER MENOS-":
                mas_perfiles.close()
                eventos_inicio()
                break
            case "-AGREGAR PERFIL-":
                mas_perfiles.close()
                nuevo_perfil.ventana_nuevo_perfil()
                break
        if evento in keys:
            menu=menu_principal.ventana_menu(datos[evento])
            mas_perfiles.close()
            menu_principal.eventos_menu_principal(menu)

def eventos_inicio():
    '''Maneja los eventos de la ventana de inicio, cuando se invoca se lee
    el archivo json de perfiles para mostrar correctamente los perfiles en
    la pantalla de inicio
    '''
    datos,keys=act.actulizar_data()

    ventana_de_inicio=generar_ventana_de_inicio(datos)

    while True:
        evento, valores = ventana_de_inicio.read()
        match evento:
            case sg.WIN_CLOSED:
                ventana_de_inicio.close()
                break
            case "-AGREGAR PERFIL-":
                ventana_de_inicio.close()
                nuevo_perfil.ventana_nuevo_perfil()
                break
            case "-VER MAS-":
                ventana_de_inicio.close()
                manejar_eventos_mas_perfiles(datos,keys)
                break
        if evento in keys:
            ventana_de_inicio.close()
            menu=menu_principal.ventana_menu(datos[evento])
            menu_principal.eventos_menu_principal(menu)
            break

if __name__ =="__main__":
     eventos_inicio()