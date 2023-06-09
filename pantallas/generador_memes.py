import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad.verificar_input import falta_completar_campos



def generar_meme():

    fuentes = sg.Text.fonts_installed_list() 
    
    '''Esta funcion define una ventana 
    para generar memes a partir de una imágen y un seleccionados por el usuario. '''
    
    columna_izquierda = [[sg.Text('Seleccionar fuente:')],
        [sg.Listbox(fuentes, size=(20, 5), change_submits=True, key='-FUENTE-')]
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

    while True:
        evento, values = window.Read()
        print(values['-FUENTE-'])
        if evento == "-VOLVER-":
            window.close()
            break
        elif evento== sg.WIN_CLOSED:
            sys.exit()
        elif evento == "-GENERAR-" :
            if not falta_completar_campos(values) :  
                #genero el meme
                sg.popup("Se generó un meme!")
                break
            else:
                sg.popup("No se completaron los campos necesarios")

if __name__ =="__main__":
    generar_meme()
