import sys
import os
import PySimpleGUI as sg
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import inicio
from pantallas import rutas
from pantallas import menu_principal
from pantallas import generador_memes
from pantallas import Generador_collage
from pantallas import etiquetar_imagenes
from pantallas import configuracion
from pantallas import nuevo_perfil

ruta_archivo = rutas.archivo_perfiles_json
ruta_repositorio_imagenes=rutas.imagenes_perfil

try:
    with open(ruta_archivo,"r",encoding="UTF-8") as archivo:
        data = json.load(archivo)
        keys=list(map(lambda i: i, range(data.__len__())))
except (FileNotFoundError,PermissionError,json.JSONDecodeError):
    data=[]

def eventos_menu_principal(menu):
    '''Maneja los eventos de la ventana menu prinicipal'''
    while True:
        evento, valores = menu.read()
        if evento==sg.WIN_CLOSED or evento=="-SALIR-":
            menu.close()
            break
        match evento:
            case "-VENTANA AYUDA-":
                if __name__ =="__main__":
                    menu_principal.generar_ventana_de_ayuda()
            case "-VENTANA MEME-":
                menu.hide()
                if __name__ =="__main__":
                    generador_memes.generar_meme()
                menu.un_hide()
            case "-VENTANA COLLAGE-":
                menu.hide()
                if __name__ =="__main__":
                    Generador_collage.generar_collage()
                menu.un_hide()
            case "-VENTANA ETIQUETAR-":
                menu.hide()
                if __name__ =="__main__":
                    etiquetar_imagenes.pantalla_etiquetar(menu.metadata["perfil_actual"]["Usuario"])
                menu.un_hide()
            case "-VENTANA CONFIGURACION-":
                menu.hide()
                if __name__ =="__main__":
                    configuracion.pantalla_configuracion(menu.metadata["perfil_actual"]["Usuario"])
                menu.un_hide()
            case "-VENTANA EDITAR PERFIL-":
                #mostrar editar perfil
                pass


def manejar_eventos_mas_perfiles(keys,datos):
    '''Maneja los eventos de la ventana que muestra todos los perfiles'''
    if __name__ =="__main__":
        mas_perfiles=inicio.mostrar_mas_perfiles(datos)
    while True:
        evento, valores = mas_perfiles.read()
        if evento==sg.WIN_CLOSED or evento=="-VER MENOS-":
            mas_perfiles.close()
            break
        elif evento=="-AGREGAR PERFIL-":
            ventana_de_inicio.hide()
            if __name__ =="__main__":
                nuevo_perfil.ventana_nuevo_perfil()
        elif evento in keys:
            if __name__ =="__main__":
                menu=menu_principal.ventana_menu(datos[evento])
            mas_perfiles.close()
            eventos_menu_principal(menu)

if __name__ =="__main__":
     ventana_de_inicio=inicio.generar_ventana_de_inicio(data)

while True:
    evento, valores = ventana_de_inicio.read()
    match evento:
        case sg.WIN_CLOSED:
            ventana_de_inicio.close()
            break
        case "-AGREGAR PERFIL-":
            ventana_de_inicio.hide()
            if __name__ =="__main__":
                nuevo_perfil.ventana_nuevo_perfil()
            ventana_de_inicio.un_hide()
        case "-VER MAS-":
            ventana_de_inicio.hide()
            manejar_eventos_mas_perfiles(keys,data)
            ventana_de_inicio.un_hide()
    if evento in keys:
        ventana_de_inicio.hide()
        if __name__ =="__main__":
           menu=menu_principal.ventana_menu(data[evento])
        eventos_menu_principal(menu)
        ventana_de_inicio.un_hide()