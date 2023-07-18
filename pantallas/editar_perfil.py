
import sys
import os
import json
import PySimpleGUI as sg
from PIL import Image

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funcionalidad.editar_perfil import *
from funcionalidad.nuevo_perfil import *
from funcionalidad.verificar_input import falta_completar_campos
from rutas import ruta_imagenes_perfil 
from rutas import archivo_perfiles_json as ruta_archivo
from funcionalidad import registrar_log

def ventana_editar_perfil(perfil_actual):
    '''Genera la ventana de editar perfil, tanto su layout como se manejador
    de eventos, recibiendo todos los datos del perfil actual, en la variable
    perfil_actual que se trata de un diccionario, para que estos sean visualizados
    en pantalla
    '''
    columna_izquierda = [
        [sg.Text("Editar perfil")],
        [sg.Text("Nombre:")],
        [sg.InputText(key="Nombre")],
        [sg.Text("Edad:")],
        [sg.Input(key="Edad", size=(10,))],
        [sg.Text("Genero:")],
        [
            sg.Listbox(
                ["Masculino", "Femenino", "Otro"],
                no_scrollbar=False,
                s=(15, 3),
                key="Genero",
                enable_events=True,
            )
        ],
        [sg.Text("Especificar genero:")],
        [sg.InputText(key="Especificar genero", disabled=True)],
        [sg.Button("Guardar", key="-GUARDAR-"), sg.Button("Volver", key="-VOLVER-")],
    ]


    columna_derecha = [
        [
            sg.Image(
                source=os.path.join(ruta_imagenes_perfil, perfil_actual["Avatar"]),
                key=("Avatar"),
                size=(300, 300),
                subsample=3,
                pad=((125, 125), (0, 0)),
            )
        ],
        [
            sg.FileBrowse(
                "Seleccionar Imagen",
                initial_folder=ruta_imagenes_perfil,
                key=("-BROWSE-"),
                enable_events=True,
                change_submits=True,
                size=(20, 2),
            ),
        ],
    ]

    layout = [
        [
            sg.Column(columna_izquierda, element_justification="c"),
            sg.VSeperator(),
            sg.Column(columna_derecha, element_justification="c"),
        ]
    ]

    window = sg.Window("Editar perfil", layout, finalize=True)

    
    if (perfil_actual is not None):
        mostrar_perfil(perfil_actual,window)

    while True:
        event, values = window.read()

        if event == "-VOLVER-":
            window.close()
            break
        elif event == sg.WIN_CLOSED:
            sys.exit()
        
        elif event == "-BROWSE-":
            filename = values["-BROWSE-"]
            window["Avatar"].update(filename,
            size=(300, 300),
            subsample=3,
            )

        elif event == "Genero":
            genero = values["Genero"][0]
            if genero == "Otro":
                window["Especificar genero"].update(disabled=False)
            else:
                window["Especificar genero"].update(disabled=True)

        elif event == "-GUARDAR-":

            try:
                with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
                    perfiles = json.load(archivo)
            except (FileNotFoundError, json.JSONDecodeError):
                sg.popup_error("""El archivo 'nuevo_perfil.json' no se encontró, la aplicacion no puede continuar y se cerrará el programa.""")
                sys.exit()
            except PermissionError:
                sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'nuevo_perfil.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
                sys.exit()

            llenar_genero(values,perfil_actual['Avatar'])
            if not falta_completar_campos(values):
                if verificar_edad(values["Edad"]):
                    perfil_modificado = modificar_perfil(perfil_actual,values)

                    perfiles_actualizados = actualizar_perfil(perfiles, perfil_modificado)
                    
                    try:
                        with open(ruta_archivo, "w") as archivo:
                            json.dump(perfiles_actualizados, archivo, indent=4)
                            sg.popup('El perfil se edito correctamente!')
                    except PermissionError:
                        sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'nuevo_perfil.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
                        sys.exit()

                    registrar_log.registrar_interaccion(perfil_actual['Usuario'],'Edito el perfil')
                    window.close()
                    return perfil_modificado
                else:
                    sg.popup("Ingresa una edad valida")
            else:
                sg.popup("Falta llenar el formulario")

    return perfil_actual
        

if __name__ == "__main__":
    ventana_editar_perfil()

