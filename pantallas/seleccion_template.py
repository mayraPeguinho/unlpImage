#!/usr/bin/env python
import sys
import os
import json
import PySimpleGUI as sg
import PIL


# Agrego el directorio raiz a la ruta de búsqueda de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad import etiquetar_imagenes as ei
from funcionalidad import configuracion as cg
from rutas import archivo_tenmplates_json as ruta_templates

from pantallas import generador_memes as ge

def pantalla_seleccionartemplate(usuario):

    #Leo desde el archivo de configuración, donde ir a buscar mi repositorio de imagenes
    starting_path = cg.obtener_directorio('repositorio_imagenes')
    #Creo el arbol visual de archivos. 
    treedata = ei.add_files_in_folder('', starting_path)

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
                    ge.generar_meme(ruta_imagen, data, usuario)
                except IndexError:
                    sg.popup_error("¡Primero debes elegir una imágen válida!")
                except PermissionError:
                    sg.popup_error("¡No tienes permisos para acceder a esa carpeta o archivo!")
                
if __name__ =="__main__":
    pantalla_seleccionartemplate("null")
