#!/usr/bin/env python
import sys
import os
import json
import PySimpleGUI as sg
import PIL


# Agrego el directorio raiz a la ruta de búsqueda de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad import etiquetar_imagenes as ei
from funcionalidad import seleccion_template as st
from funcionalidad import configuracion as cg
from rutas import archivo_configuracion_json as ruta_archivo
from rutas import archivo_tenmplates_json as ruta_templates
from rutas import directorio_padre
from pantallas import generador_memes as ge

def pantalla_seleccionartemplate(usuario):

    folder_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABnUlEQVQ4y8WSv2rUQRSFv7vZgJFFsQg2EkWb4AvEJ8hqKVilSmFn3iNvIAp21oIW9haihBRKiqwElMVsIJjNrprsOr/5dyzml3UhEQIWHhjmcpn7zblw4B9lJ8Xag9mlmQb3AJzX3tOX8Tngzg349q7t5xcfzpKGhOFHnjx+9qLTzW8wsmFTL2Gzk7Y2O/k9kCbtwUZbV+Zvo8Md3PALrjoiqsKSR9ljpAJpwOsNtlfXfRvoNU8Arr/NsVo0ry5z4dZN5hoGqEzYDChBOoKwS/vSq0XW3y5NAI/uN1cvLqzQur4MCpBGEEd1PQDfQ74HYR+LfeQOAOYAmgAmbly+dgfid5CHPIKqC74L8RDyGPIYy7+QQjFWa7ICsQ8SpB/IfcJSDVMAJUwJkYDMNOEPIBxA/gnuMyYPijXAI3lMse7FGnIKsIuqrxgRSeXOoYZUCI8pIKW/OHA7kD2YYcpAKgM5ABXk4qSsdJaDOMCsgTIYAlL5TQFTyUIZDmev0N/bnwqnylEBQS45UKnHx/lUlFvA3fo+jwR8ALb47/oNma38cuqiJ9AAAAAASUVORK5CYII='
    file_icon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAABU0lEQVQ4y52TzStEURiHn/ecc6XG54JSdlMkNhYWsiILS0lsJaUsLW2Mv8CfIDtr2VtbY4GUEvmIZnKbZsY977Uwt2HcyW1+dTZvt6fn9557BGB+aaNQKBR2ifkbgWR+cX13ubO1svz++niVTA1ArDHDg91UahHFsMxbKWycYsjze4muTsP64vT43v7hSf/A0FgdjQPQWAmco68nB+T+SFSqNUQgcIbN1bn8Z3RwvL22MAvcu8TACFgrpMVZ4aUYcn77BMDkxGgemAGOHIBXxRjBWZMKoCPA2h6qEUSRR2MF6GxUUMUaIUgBCNTnAcm3H2G5YQfgvccYIXAtDH7FoKq/AaqKlbrBj2trFVXfBPAea4SOIIsBeN9kkCwxsNkAqRWy7+B7Z00G3xVc2wZeMSI4S7sVYkSk5Z/4PyBWROqvox3A28PN2cjUwinQC9QyckKALxj4kv2auK0xAAAAAElFTkSuQmCC'

    #Leo desde el archivo de configuración, donde ir a buscar mi repositorio de imagenes

    starting_path = cg.obtener_directorio('repositorio_imagenes')

    #Declaro la ruta del csv de donde leo y guardo los datos de las imagenes
    #para poder mostrar los archivos en forma de cascada hay que usar un objeto "treedata" incluído en PySimplegui
    #lo extraje de la documentación oficinal de sg
    treedata = sg.TreeData()

    #Creo el arbol visual de archivos. 
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


    columna_izquierda = [[sg.Text('Seleccionar template')],
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
                    )],
            [sg.Button('Generar'), sg.Button('Volver')]]

    columna_derecha = [[sg.Text('Previsualización:')],
                [sg.Text(size=(40,1), key='-TOUT-')],
                [sg.Image(key='-IMAGE-', size= (15, 20))]]

    layout = [[sg.Column(columna_izquierda, element_justification='c'), sg.VSeperator(),sg.Column(columna_derecha, element_justification='c')]]


    #agregar en window el manejo de usuarios entre ventanas. 
    window = sg.Window('Generar meme', layout, resizable=False, finalize=True)


    while True:     # Loop de eventos
        with open(ruta_templates) as archivo:
            data = json.load(archivo)
        rutas_imagenes = [item['image'] for item in data]

         
        event, values = window.read()    
        if event == 'Volver':
            window.close()
            break
        elif event == sg.WIN_CLOSED:
            sys.exit()           
        else:
            if event == '-TREE-':
                
                #Chequear que se pueda abrir y tratar la imagen
                try:
                   
                    # traigo la ruta de la imagen
                    ruta_imagen = values['-TREE-'][0].replace("\\", "/")
                    
                    if os.path.basename(ruta_imagen) in rutas_imagenes:
                        datavisual_imagen = ei.mostrar_imagen(ruta_imagen)
                        window["-IMAGE-"].update(data=datavisual_imagen)
                    else:
                        sg.popup_error("¡No es un template!")
                

                except PIL.UnidentifiedImageError:
                    sg.popup_error("¡No es una imagen!")
                except IsADirectoryError:
                    pass
                except PermissionError:
                    sg.popup_error("¡No tienes permisos para acceder a esa carpeta!")
            if event == 'Generar':
                try:
                    window.hide() 
                    ge.generar_meme(ruta_imagen, data, usuario)
                    window.un_hide()
                except IndexError:
                    sg.popup_error("¡Primero debes elegir una imágen válida!")
                
if __name__ =="__main__":
    pantalla_seleccionartemplate("null")
