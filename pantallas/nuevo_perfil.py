import sys
import os
import json
import PySimpleGUI as sg
from PIL import Image

ruta_imagen = os.path.join(os.getcwd(),'imagenes','imagenes_perfil', 'avatar.png')

ruta_archivo = os.path.join(os.getcwd(),'datos', 'perfil_nuevo.json')

columna_izquierda = [[sg.Text('Nuevo perfil')],
          [sg.Text('Usuario:')],[sg.InputText(key='-USUARIO-'), sg.Button('Validar', key='-VALIDAR-')], 
          [sg.Text('Nombre:')],[sg.InputText(key='-NOMBRE-')],
          [sg.Text('Edad:')],[sg.InputText(key='-EDAD-')],
          [sg.Text('Genero:')],
          [sg.Listbox(['Masculino', 'Femenino', 'Otro'],no_scrollbar=False, s=(15,3),key='-GENERO-')],
             [sg.InputText(key='-ESPECIFICAR_GENERO-')],
          [sg.Button('Guardar', key='-GUARDAR-'), sg.Button('Volver', key='-VOLVER-')]]



columna_derecha =   [
                    [
                        sg.Image(
                            source=ruta_imagen,
                            key=('-AVATAR-'),
                            size=(60,60),
                            pad=((125,125), (0,0)),
                        )
                    ],
                    [
                        sg.FileBrowse(
                            "Seleccionar Imagen",
                            key=('-BROWSE-'),
                            enable_events=True,
                            change_submits=True,
                            size=(20,2),
                        ),   
                    ],
                    ]

layout = [[sg.Column(columna_izquierda, element_justification='c'), sg.VSeperator(),sg.Column(columna_derecha, element_justification='c')]]

window = sg.Window('Nuevo perfil', layout)

while True:
    event, values = window.read()
    print(values)
    if event == '-VOLVER-' or event == sg.WIN_CLOSED:
        break
    elif event == '-BROWSE-':
        filename = values['-BROWSE-']
        window['-AVATAR-'].update(
           source=filename,
           size=(60,60),
        )
    elif event == '-VALIDAR-':
        with open(ruta_archivo, 'r') as archivo:
            datos_perfil = json.load(archivo)
        mostrar_datos = json.dumps(datos_perfil, indent=4)
        print(mostrar_datos)
        #mostrar_datos[0] == '-USUARIO-':
        #   sg.popup('Usuario existente, ingrese otro usuario')
    elif event == '-GUARDAR-':      
       with open(ruta_archivo, 'a') as archivo:
           json.dump(values, archivo)
           print('Se creo el archivo')
            

window.close()
