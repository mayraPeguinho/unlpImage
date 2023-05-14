import sys
import os
import PySimpleGUI as sg
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import inicio
from pantallas import rutas
from pantallas import menu_principal
from pantallas import nuevo_perfil

ruta_archivo = rutas.archivo_perfiles_json
ruta_repositorio_imagenes=rutas.imagenes_perfil

try:
    with open(ruta_archivo,"r",encoding="UTF-8") as archivo:
        data = json.load(archivo)
    keys=list(map(lambda i: i, range(data.__len__())))
except (FileNotFoundError,PermissionError,json.JSONDecodeError):
    data=[]

ventana_de_inicio=inicio.generar_ventana_de_inicio(data)

while True:
    evento, valores = ventana_de_inicio.read()
    match evento:
        case sg.WIN_CLOSED:
            ventana_de_inicio.close()
            break
        case "-AGREGAR PERFIL-":
            ventana_de_inicio.hide()
            nuevo_perfil.ventana_nuevo_perfil()
            ventana_de_inicio.un_hide()
        case "-VER MAS-":
            ventana_de_inicio.hide()
            inicio.manejar_eventos_mas_perfiles(keys,data)
            ventana_de_inicio.un_hide()
    if evento in keys:
        ventana_de_inicio.hide()
        menu=menu_principal.ventana_menu(data[evento])
        menu_principal.eventos_menu_principal(menu)
        ventana_de_inicio.un_hide()