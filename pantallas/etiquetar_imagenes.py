#!/usr/bin/env python
import sys
import os
import json
import PySimpleGUI as sg
from PIL import Image, ImageTk
folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'


ruta_archivo = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')), 'configuracion.json')

#el siguiente if valida si ya está creado un archivo de configuración. Podría ir en funcionalidad
#otro problema es que si entra en el else "starting_path" no se crea nunca. Solucionar con excepciones
if os.path.exists(ruta_archivo):
    print("El archivo existe")
    with open(ruta_archivo) as f:
        data = json.load(f)
        starting_path = data['repositorio_imagenes']
else:
    layout= [[sg.Text("¡Parece que aún no has configurado tu repositorio de imágenes! ¿Deseas configurarlo ahora?")],
            [sg.OK(button_text="Si"), sg.Cancel(button_text="No")]]
    window = sg.Window("¡Advertencia!", layout, margins=(100, 50))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'No':
            break
        if event == 'Si':
            ruta_pantallaconfig = os.path.abspath(os.path.join(os.path.dirname(__file__), 'configuracion.py'))
            import subprocess
            subprocess.run(["python", ruta_pantallaconfig])
            sys.exit()
            break
    window.close()


#para poder mostrar los archivos en forma de cascada hay que usar un objeto "treedata" incluído en PySimplegui
treedata = sg.TreeData()


def add_files_in_folder(parent, dirname):
    files = os.listdir(dirname)
    for f in files:
        fullname = os.path.join(dirname, f)
        if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
            treedata.Insert(parent, fullname, f, values=[], icon=folder_icon)
            add_files_in_folder(fullname, fullname)
        else:
            treedata.Insert(parent, fullname, f, values=[os.stat(fullname).st_size], icon=file_icon)

add_files_in_folder('', starting_path)



columna_izquierda = [[sg.Text('Repositorio de imagenes')],
          [sg.Tree(data=treedata,
                   headings=['Tamaño', ],
                   auto_size_columns=True,
                   select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                   num_rows=20,
                   col0_width=40,
                   key='-TREE-',
                   show_expanded=False,
                   enable_events=True,
                   expand_x=True,
                   expand_y=True,
                   ),],
          [sg.Text('Tag:')], 
          [sg.InputText(key='Tag'),sg.Button('Agregar')],
          [sg.Text('Texto descriptivo:')], 
          [sg.InputText(key='Texto'),sg.Button('Agregar')],
          [sg.Button('Guardar'), sg.Button('Volver')]]



columna_derecha = [[sg.Text('La imagen que elegiste:')],
              [sg.Text(size=(40,1), key='-TOUT-')],
              [sg.Image(key='-IMAGE-')]]
              

layout = [[sg.Column(columna_izquierda, element_justification='c'), sg.VSeperator(),sg.Column(columna_derecha, element_justification='c')]]

window = sg.Window('Etiquetar Imagenes', layout, resizable=True, finalize=True)

imagen_seleccionada = {'ruta': '', 'tag': '', 'descripcion': ''}
ruta_archivo_imagenes = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')), 'etiquetas_imagenes.json')


while True:     # Event Loop
    event, values = window.read()    
    if event in (sg.WIN_CLOSED, 'Volver'):
        break
    else:
        if event == '-TREE-':
            # Obtener la ruta de la imagen seleccionada
            ruta_imagen = values['-TREE-'][0]
            # Actualizar la variable imagen_seleccionada
            imagen_seleccionada['ruta'] = ruta_imagen
            # Cargar y mostrar la imagen en la columna de la derecha
            if ruta_imagen.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                imagen = sg.Image(filename=ruta_imagen, size=(300, 300))
                window['-IMAGE-'].update(imagen)
            # Actualizar la etiqueta de texto de la imagen seleccionada en la columna de la derecha
            window['-TOUT-'].update(os.path.basename(ruta_imagen))
            imagen = Image.open(os.path.join(ruta_imagen))
            ruta_imagen = values['-TREE-'][0]
            imagen = Image.open(ruta_imagen)
            # convertir la imagen a un formato que pueda mostrar PySimpleGUI
            tk_img = ImageTk.PhotoImage(imagen)
            window["-IMAGE-"].update(data=tk_img)


            
        if event == 'Agregar':
            imagen_seleccionada['tag'] = values['Tag']
            imagen_seleccionada['descripcion'] = values['Texto']
        if event == 'Guardar':
            # Obtener el archivo JSON de configuración
            with open(ruta_archivo) as f:
                data = json.load(f)
            # Actualizar los datos de la imagen seleccionada en el archivo JSON
            data['imagenes'][imagen_seleccionada['ruta']] = {'tag': imagen_seleccionada['tag'], 'descripcion': imagen_seleccionada['descripcion']}
            # Guardar los cambios en el archivo JSON
            with open(ruta_archivo_imagenes, 'w') as f:
                json.dump(data, f)
            print(event, values)

window.close()



