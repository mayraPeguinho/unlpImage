import PySimpleGUI as sg
import sys
import os
import json
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from funcionalidad.verificar_input import falta_completar_campos
import rutas as r
from funcionalidad.crear_meme import *

def definir_layout(cant_cajas):
    """Se arma de que manera puede ser la interfaz dependiendo la cantidad
    de cajas de texto se tiene"""

    
    if cant_cajas == 1:
        columna_izquierda = [
            [sg.Text("Seleccionar fuente:")],
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-')],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Button("Actualizar", key=("-ACTUALIZAR-"))],
        ]
    elif cant_cajas == 2:
        columna_izquierda = [
            [sg.Text("Seleccionar fuente:")],
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-')],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Text('Texto 2:')],[sg.Input(key = '-TEXTO_2-')],
            [sg.Button("Actualizar", key=("-ACTUALIZAR-"))],
        ]
    elif cant_cajas == 3:
        columna_izquierda = [
            [sg.Text("Seleccionar fuente:")],
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-')],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Text('Texto 2:')],[sg.Input(key = '-TEXTO_2-')],
            [sg.Text('Texto 3:')],[sg.Input(key = '-TEXTO_3-')],
            [sg.Button("Actualizar", key=("-ACTUALIZAR-"))],
        ]
    elif cant_cajas == 4:
        columna_izquierda = [
            [sg.Text("Seleccionar fuente:")],
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-')],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Text('Texto 2:')],[sg.Input(key = '-TEXTO_2-')],
            [sg.Text('Texto 3:')],[sg.Input(key = '-TEXTO_3-')],
            [sg.Text('Texto 4:')],[sg.Input(key = '-TEXTO_4-')],
            [sg.Button("Actualizar", key=("-ACTUALIZAR-"))],
        ]
    elif cant_cajas == 5:
        columna_izquierda = [
            [sg.Text("Seleccionar fuente:")],
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-')],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Text('Texto 2:')],[sg.Input(key = '-TEXTO_2-')],
            [sg.Text('Texto 3:')],[sg.Input(key = '-TEXTO_3-')],
            [sg.Text('Texto 4:')],[sg.Input(key = '-TEXTO_4-')],
            [sg.Text('Texto 5:')],[sg.Input(key = '-TEXTO_5-')],
            [sg.Button("Actualizar", key=("-ACTUALIZAR-"))],
        ]

    columna_derecha = [
        [sg.Image(key="-IMAGEN-", size=(200, 200))],
        [
            sg.Column(
                [[sg.Button("Guardar", key="-GUARDAR-")]],
                expand_x=True,
                element_justification="right",
            )
        ],
    ]

    layout = [
        [
            sg.Column(columna_izquierda, element_justification="c"),
            sg.VSeperator(),
            sg.Column(columna_derecha, element_justification="c"),
        ]
    ]

    return layout


def generar_meme(imagen_seleccionada,meme_json,usuario):

    meme_json = [item for item in meme_json if item['image'] == os.path.basename(imagen_seleccionada)]

    cant_cajas = (meme_json[0]['text_boxes'].__len__())

    layout = definir_layout(cant_cajas)

    window = sg.Window(
        "Generador de memes", layout, margins=(60, 80), finalize=True, resizable=True
    )
    """Muestro el meme que se me pasa por parametro"""

    cargar_meme = PIL.Image.open(imagen_seleccionada)

    imagen_meme = PIL.ImageTk.PhotoImage(cargar_meme)
    window["-IMAGEN-"].update(data=imagen_meme)

    while True:
        event, values = window.Read()
        print(values)
        window
        if event == "-VOLVER-":
            window.close()
            break

        elif event == sg.WIN_CLOSED:
            sys.exit()

        elif event == "-ACTUALIZAR-":
            print(values)
            meme_actual = actualizar_datos(cargar_meme,meme_json,values)
            
            imagen_meme = PIL.ImageTk.PhotoImage(meme_actual)
            window["-IMAGEN-"].update(data=imagen_meme)

        elif event == "-GENERAR-":
            if not falta_completar_campos(values):
                # genero el meme
                
                sg.popup("Se generó un meme!")
                break
            else:
                sg.popup("No se completaron los campos necesarios")


if __name__ == "__main__":
    generar_meme(imagen_seleccionada,meme_json,usuario)
