import PySimpleGUI as sg
import sys
import os
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad.verificar_input import falta_completar_campos
import rutas as r
from funcionalidad.crear_meme import *


ruta_avatares= os.path.join(r.ruta_imagenes_perfil,'hombre_traje.png')

def generar_meme():

    fuentes = sg.Text.fonts_installed_list() 
    
    '''Esta funcion define una ventana 
    para generar memes a partir de una imágen y un seleccionados por el usuario. '''
    
    columna_izquierda = [[sg.Text('Seleccionar fuente:')],
        [sg.Listbox(fuentes, size=(20, 5), change_submits=True, key='-FUENTE-')],
        [sg.Button('Actualizar', key=('-ACTUALIZAR-'))]
    ]


    columna_derecha = [
         [sg.Image(key="-IMAGEN-", size=(200, 200))],
         [sg.Column(
         [[sg.Button("Guardar", key="-GUARDAR-")]],
                     expand_x=True,
                     element_justification="right"
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
    window = sg.Window('Generador de memes',layout, margins=(60, 80), finalize=True, resizable=True)

    """Muestro el meme que se me pasa por parametro"""
    cargar_meme = PIL.Image.open(ruta_avatares)

    imagen_meme = PIL.ImageTk.PhotoImage(cargar_meme)
    window['-IMAGEN-'].update(data=imagen_meme)


    while True:
        event, values = window.Read()
        print(values['-FUENTE-'])
        window
        if event == "-VOLVER-":
            window.close()
            break

        elif event== sg.WIN_CLOSED:
            sys.exit()
        
        elif event == '-ACTUALIZAR-':
            meme_actual = actualizar_datos(imagen_meme)
    
        elif event == "-GENERAR-" :
            if not falta_completar_campos(values) :  
                #genero el meme
                sg.popup("Se generó un meme!")
                break
            else:
                sg.popup("No se completaron los campos necesarios")

if __name__ =="__main__":
    generar_meme()
