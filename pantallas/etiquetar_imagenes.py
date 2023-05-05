#!/usr/bin/env python
import sys
import os
import json
import PySimpleGUI as sg
import PIL
from PIL import Image, ImageTk
import csv
folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

ruta_archivo = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')), 'configuracion.json')
#se va el tryexcept, trabajar con valores por defecto 
try:
    with open(ruta_archivo) as f:
        data = json.load(f)
        starting_path = data['repositorio_imagenes']
except FileNotFoundError:
    layout= [[sg.Text("¡Parece que aún no has configurado tu repositorio de imágenes! ¿Deseas configurarlo ahora?")],
            [sg.OK(button_text="Si"), sg.Cancel(button_text="No")]]
    window = sg.Window("¡Advertencia!", layout, margins=(100, 50))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'No':
            break
            window.close()
        if event == 'Si':
            ruta_pantallaconfig = os.path.abspath(os.path.join(os.path.dirname(__file__), 'configuracion.py'))
            import subprocess
            subprocess.run(["python", ruta_pantallaconfig])
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
              [sg.Image(key='-IMAGE-', size= (15, 20))],
              [sg.Text('Descripción: ', key='-DESCRIPCION-')]]
              

layout = [[sg.Column(columna_izquierda, element_justification='c'), sg.VSeperator(),sg.Column(columna_derecha, element_justification='c')]]


#agregar en window el manejo de usuarios entre ventanas. 
window = sg.Window('Etiquetar Imagenes', layout, resizable=False, finalize=True)

imagen_seleccionada = {'ruta': '', 'tag': '', 'descripcion': ''}
ruta_archivo_imagenes = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')), 'etiquetas_imagenes.json')


while True:     # Loop de eventos
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
                imagen = sg.Image(filename=ruta_imagen)
                window['-IMAGE-'].update(imagen)
            # Actualizar la etiqueta de texto de la imagen seleccionada en la columna de la derecha
            window['-TOUT-'].update(os.path.basename(ruta_imagen))

             #Chequear que se pueda abrir la imagen
            try:
                imagen = Image.open(os.path.join(ruta_imagen))
                ruta_imagen = values['-TREE-'][0]
                imagen = Image.open(ruta_imagen).resize((350, 300))
                #Extraigo los metadatos de la imagen
                metadata = imagen.getexif()
                # convertir la imagen a un formato que pueda mostrar PySimpleGUI
                tk_img = ImageTk.PhotoImage(imagen)
                window["-IMAGE-"].update(data=tk_img)
            except PIL.UnidentifiedImageError:
                sg.popup("¡No es una imagen!")
            except PermissionError:
                sg.popup("¡No tienes permisos para acceder a esa carpeta!")

            


        #Eventos    
        if event == 'Agregar':
            imagen_seleccionada['tag'] = values['Tag']
            imagen_seleccionada['descripcion'] = values['Texto']

        #ver como guardar la metadata
        if event == 'Guardar':
            # Obtener el archivo CSV de etiquetas y descripciones con:  
                #Ruta relativa a la imagen (metadata)
                #Texto descriptivo (lo saco de imagen_seleccionada)
                #resolucion (metadata)
                #tamaño (metadata)
                #tipo (mimetype)
                #lista de tags(lo saco de imagen_seleccionada)
                #ultimo perfil que actualizó ---(/!\ ver con Fran como implementar esta funcionalidad)---
                #Fecha de ultima actualización (extraer del log)

            ruta_csv = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')), 'imagenes_etiquetadas.csv')

            #Verificar que exista el csv, si no existe debo crearlo. ¿Es esto necesario?
            try:
                with open('../datos/imagenes_etiquetadas.csv', 'r+') as f:
                    pass
                    
            except FileNotFoundError:
                open('../datos/imagenes_etiquetadas.csv', 'w')

           
window.close()



