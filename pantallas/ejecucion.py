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

ruta_archivo = rutas.archivo_perfiles_json
ruta_repositorio_imagenes=rutas.imagenes_perfil

data={}
keys=[]
try:
    with open(ruta_archivo,"r") as archivo:
        data = json.load(archivo)
        i=0
        for elem in data:
            keys.append(i)
            i=i+1
except FileNotFoundError:
    x=1
except PermissionError:
    x=2
except Exception:
    x=3

def eventos_menu_principal(menu):
    #Maneja los eventos de la ventana menu prinicipal
    while True:
        evento, valores = menu.read()
        match evento:
            case sg.WIN_CLOSED:
                menu.close()
                break
            case "Salir":
                menu.close()
                break
            case "?":
                if __name__ =="__main__":
                    menu_principal.generar_ventana_de_ayuda(menu)
            case "Generar meme":
                menu.hide()
                if __name__ =="__main__":
                    generador_memes.generar_meme()
                menu.un_hide()
            case "Generar collage":
                menu.hide()
                if __name__ =="__main__":
                    Generador_collage.generar_collage()
                menu.un_hide()
            case "Etiquetar imagenes":
                #mostrar etiquetar imagenes
                x=1
            case "Configuracion":
                #mostrar configuracion
                x=1
            case "Perfil":
                #mostrar editar perfil
                x=1


def manejar_eventos_mas_perfiles(keys,ventana_de_inicio,datos):
    if __name__ =="__main__":
        mas_perfiles=inicio.mostrar_mas_perfiles(datos)
    while True:
        evento, valores = mas_perfiles.read()
        match evento:
            case sg.WIN_CLOSED:
                mas_perfiles.close()
                break
            case "Ver menos":
                mas_perfiles.close()
                break
            case "+":
                #Va la pestaña de nuevo perfil
                x=1
        if evento in keys:
            ventana_de_inicio.metadata["perfil_actual"]=datos[evento]
            if __name__ =="__main__":
                menu=menu_principal.ventana_menu(ventana_de_inicio.metadata["perfil_actual"]["-BROWSE-"])
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
        case "+":
            #Va la pestaña de nuevo perfil
            x=1
        case "Ver más":
            ventana_de_inicio.hide()
            manejar_eventos_mas_perfiles(keys,ventana_de_inicio,data)
            ventana_de_inicio.un_hide()
    if evento in keys:
        ventana_de_inicio.metadata["perfil_actual"]=data[evento]
        ventana_de_inicio.hide()
        if __name__ =="__main__":
           menu=menu_principal.ventana_menu(ventana_de_inicio.metadata["perfil_actual"]["-BROWSE-"])
        eventos_menu_principal(menu)
        ventana_de_inicio.un_hide()