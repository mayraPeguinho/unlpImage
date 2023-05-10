import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import rutas

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

def ventana_menu(imagen,usuario):
    '''Esta funcion define la ventana de menu. '''
    columna1=[[sg.Button(image_source=os.path.join(rutas.imagenes_perfil,imagen),image_size=(80,80),image_subsample=3,key="VENTANA EDITAR PERFIL")],
              [sg.Text(usuario)]
             ]
    columna2=[[sg.Button("Configuracion",key="-VENTANA CONFIGURACION-")]]
    
    columna3=[[sg.Button('?',tooltip="Ayuda",key="-VENTANA AYUDA-")]]

    layout = [[sg.Column(columna1),sg.Column(columna2),sg.Column(columna3)],
              [sg.Button("Etiquetar Imagenes",key="-VENTANA ETIQUETAR-")],
              [sg.Button("Generar meme",key="-VENTANA MEME-")],
              [sg.Button("Generar collage",key="-VENTANA COLLAGE-")],
              [sg.Button("Salir",key="-SALIR-")]
            ]
    
    return sg.Window("UNLPImage",layout,margins=(150, 150),metadata={"perfil_actual":None})

if __name__ =="__main__":
    ventana_menu()
                 