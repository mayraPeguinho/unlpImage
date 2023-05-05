#!/usr/bin/env python
import sys
import os
import json
import PySimpleGUI as sg
import PIL
from PIL import Image, ImageTk
from datetime import datetime
import mimetypes

import csv
folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

ruta_archivo = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')), 'configuracion.json')
#se va el tryexcept, trabajar con valores por defecto 

with open(ruta_archivo) as f:
    data = json.load(f)
    starting_path = data['repositorio_imagenes']

#para poder mostrar los archivos en forma de cascada hay que usar un objeto "treedata" incluído en PySimplegui
#lo extraje de la documentación oficinal de sg
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

                #Crear función tostring que me devuelva todos los datos de la imagen
                #window["-DESCRIPCION-"].update(csv_tostring(ruta_imagen))

                window["-DESCRIPCION-"].update("Esta es una descripción")

            except PIL.UnidentifiedImageError:
                sg.popup("¡No es una imagen!")
            except PermissionError:
                sg.popup("¡No tienes permisos para acceder a esa carpeta!")

            


        #Eventos    
        if event == 'Agregar':
            imagen_seleccionada['tag'] = values['Tag']
            imagen_seleccionada['descripcion'] = values['Texto']

        
        if event == 'Guardar':
            #Ruta relativa a la imagen (metadata)
            ruta = ruta_imagen 
            #Texto descriptivo (lo saco de imagen_seleccionada)
            descripcion = imagen_seleccionada['descripcion']
            #lista de tags(lo saco de imagen_seleccionada)
            tags = imagen_seleccionada['tags']
            #resolucion (metadata)
            resolucion = imagen.size
            #tipo (mimetype)
            mimetype = mimetypes.guess_type(imagen)[0]
            #tamaño (metadata)
            tamaño = os.path.getsize(imagen)
            #Fecha de ultima actualización (enviar al log)
            timestamp = datetime.timestamp(datetime.now())
            ultima_actualizacion = datetime.fromtimestamp(timestamp)
            #actualizar log  
            #            
            #ultimo perfil que actualizó ---(/!\ ver con Fran como implementar esta funcionalidad)---

            #----cargar datos en el csv, buscando por ruta_imagen y reemplazando los valores de forma adecuada----

            # Abro archivo.csv en modo lectura y escritura
            ruta_csv = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')), 'imagenes_etiquetadas.csv')
            with open(ruta_csv, mode='r+', newline='') as file:
                # Creo objeto lector
                reader = csv.DictReader(file)
                # Leo el contenido del archivo.csv y guardo la fila 
                contenido = list(reader)

                # Recorrer los datos
                for fila in contenido:
                    # Si la ruta de la imagen coincide con la ruta dada
                    if fila['ruta'] == ruta_imagen:
                        # Actualizo los valores correspondientes
                        fila['descripcion'] = descripcion
                        fila['tags'] = tags
                        fila['resolucion'] = str(resolucion[0]) + 'x' + str(resolucion[1]) #La muestro en un formato mas descriptivo
                        fila['mimetype'] = mimetype
                        fila['tamaño'] = round(tamaño / (1024*1024), 2) # tamaño en MB con 2 decimales
                        fila['ultima_actualizacion'] = ultima_actualizacion()
                        #agregar ultimo perfil que actualizó
                        break
                else:
                    # Si no se encontró una fila con la ruta dada, agreo una nueva fila (nueva imagen editada)
                    fila_nueva = {'ruta': ruta_imagen,
                                'descripcion': descripcion,
                                'tags': tags,
                                'resolucion': str(resolucion[0]) + 'x' + str(resolucion[1]), #La muestro en un formato mas descriptivo
                                'mimetype': mimetype,
                                'tamaño': round(tamaño / (1024*1024), 2), # tamaño en MB con 2 decimales
                                'ultima_actualizacion': ultima_actualizacion()
                                #agregar ultimo perfil que actualizó
                                
                                }
                    contenido.append(fila_nueva)

 
window.close()



