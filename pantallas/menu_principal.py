import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import menu_principal
from pantallas import generador_memes
from pantallas import generador_collage
from pantallas import etiquetar_imagenes
from pantallas import configuracion
from pantallas import editar_perfil

def generar_ventana_de_ayuda():
    '''Esta funcion define la ventana de ayuda
       donde se explica la funcionalidad de la aplicacion al usuario. '''
    layout = [[sg.Text("UNLPImage es una aplicación de escritorio, que permite realizar memes")],
              [sg.Text("o collages con imagenes almacenadas en el dispositivo.")]
             ]
    ventana_de_ayuda=sg.Window("Ayuda",layout)
    while True:
        evento, valores = ventana_de_ayuda.read()
        if evento == sg.WIN_CLOSED:
            ventana_de_ayuda.close()
            break

def ventana_menu(perfil_actual):
    '''Esta funcion define la ventana de menu. '''
    ruta_imagenes_perfil=os.path.join(os.getcwd(),'imagenes','imagenes_perfil')
    columna1=[[sg.Button(image_source=os.path.join(ruta_imagenes_perfil,perfil_actual["Avatar"]),
                         image_size=(80,80),
                         image_subsample=3,
                         key="-VENTANA EDITAR PERFIL-")],
              [sg.Text(perfil_actual["Usuario"])]
             ]
    columna2=[[sg.Button("Configuracion",key="-VENTANA CONFIGURACION-")]]
    
    columna3=[[sg.Button('?',tooltip="Ayuda",key="-VENTANA AYUDA-")]]

    layout = [[sg.Column(columna1),sg.Column(columna2),sg.Column(columna3)],
              [sg.Button("Etiquetar Imagenes",key="-VENTANA ETIQUETAR-")],
              [sg.Button("Generar meme",key="-VENTANA MEME-")],
              [sg.Button("Generar collage",key="-VENTANA COLLAGE-")],
              [sg.Button("Salir",key="-SALIR-")]
             ]
    
    return sg.Window("UNLPImage",layout,margins=(150, 150),metadata={"perfil_actual":perfil_actual})

def eventos_menu_principal(menu):
    '''Maneja los eventos de la ventana menu prinicipal'''
    while True:
        evento, valores = menu.read()
        match evento:
            case sg.WIN_CLOSED:
                sys.exit()
            case "-SALIR-":
                menu.close()
                break
            case "-VENTANA AYUDA-":
                menu_principal.generar_ventana_de_ayuda()
            case "-VENTANA MEME-":
                menu.hide()
                generador_memes.generar_meme()
                menu.un_hide()
            case "-VENTANA COLLAGE-":
                menu.hide()
                generador_collage.generar_collage()
                menu.un_hide()
            case "-VENTANA ETIQUETAR-":
                menu.hide()
                etiquetar_imagenes.pantalla_etiquetar(menu.metadata["perfil_actual"]["Usuario"])
                menu.un_hide()
            case "-VENTANA CONFIGURACION-":
                menu.hide()
                configuracion.pantalla_configuracion(menu.metadata["perfil_actual"]["Usuario"])
                menu.un_hide()
            case "-VENTANA EDITAR PERFIL-":
                menu.hide()
                menu.metadata["perfil_actual"]=editar_perfil.ventana_editar_perfil(menu.metadata["perfil_actual"])
                menu.un_hide()

if __name__ =="__main__":
    ventana_menu()
                 