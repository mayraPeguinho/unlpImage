import sys
import os
import PySimpleGUI as sg
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import inicio
from pantallas import rutas
from pantallas import menu_principal
from pantallas import generador_memes
from pantallas import generador_collage

ruta_archivo = rutas.archivo_perfiles_json
ruta_repositorio_imagenes=rutas.imagenes_perfil

data=[]
keys=[]
try:
    with open(ruta_archivo,"r",encoding="UTF-8") as archivo:
        data = json.load(archivo)
        i=0
        for elem in data:
            keys.append(i)
            i=i+1
except (FileNotFoundError,PermissionError,json.JSONDecodeError):
    pass

def eventos_menu_principal(menu):
    #Maneja los eventos de la ventana menu prinicipal
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
                    generador_collage.generar_collage()
                menu.un_hide()
            case "-VENTANA ETIQUETAR-":
                #ABRIR PANTALLA Y ENVIAR COMO PARÁMETRO EL NOMBRE DEL USUARIO EN FORMATO STRING
                pass
            case "-VENTANA CONFIGURACION-":
                #ABRIR PANTALLA Y ENVIAR COMO PARÁMETRO EL NOMBRE DEL USUARIO EN FORMATO STRING
                pass
            case "-VENTANA EDITAR PERFIL-":
                #mostrar editar perfil
                pass


def manejar_eventos_mas_perfiles(keys,ventana_de_inicio,datos):
    #Maneja los eventos de la ventana que muestra todos los perfiles
    if __name__ =="__main__":
        mas_perfiles=inicio.mostrar_mas_perfiles(datos)
    while True:
        evento, valores = mas_perfiles.read()
        if evento==sg.WIN_CLOSED or evento=="-VER MENOS-":
            mas_perfiles.close()
            break
        elif evento=="-AGREGAR PERFIL-":
            #Va la pestaña de nuevo perfil
            pass
        elif evento in keys:
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
        case "-AGREGAR PERFIL-":
            #Va la pestaña de nuevo perfil, cuando aprieta guardar, se despliega el  menu con ese perfil
            pass
        case "-VER MAS-":
            ventana_de_inicio.hide()
            manejar_eventos_mas_perfiles(keys,ventana_de_inicio,data)
            ventana_de_inicio.un_hide()
    if evento in keys:
        ventana_de_inicio.metadata["perfil_actual"]=data[evento]
        ventana_de_inicio.hide()
        if __name__ =="__main__":
           menu=menu_principal.ventana_menu(ventana_de_inicio.metadata["perfil_actual"]["-BROWSE-"],ventana_de_inicio.metadata["perfil_actual"]["-USUARIO-"])
        eventos_menu_principal(menu)
        ventana_de_inicio.un_hide()