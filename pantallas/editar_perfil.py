import sys
import os
import json
import PySimpleGUI as sg
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcionalidad.editar_perfil import *
from funcionalidad.nuevo_perfil import *
from pantallas import menu_principal

def ventana_editar_perfil(perfil_actual):

    ruta_imagenes_perfil= os.path.join(os.getcwd(),'imagenes','imagenes_perfil')
    image_filename=os.path.join(ruta_imagenes_perfil,perfil_actual["Avatar"])

    ruta_archivo = os.path.join(os.getcwd(), "datos", "nuevo_perfil.json")

    columna_izquierda = [
        [sg.Text("Editar perfil")],
        [sg.Text("Nombre:")],
        [sg.InputText(key='Nombre')],
        [sg.Text("Edad:")],
        [sg.Input(key="Edad", size=(10,))],
        [sg.Text("Genero:")],
        [
            sg.Listbox(
                ["Masculino", "Femenino", "Otro"],
                default_values=[perfil_actual['Genero']],
                no_scrollbar=False,
                s=(15, 3),
                key="Genero",
            )
        ],
        [sg.Text("Especificar genero:")],
        [sg.InputText(key="Especificar genero")],
        [sg.Button("Guardar", key="-GUARDAR-"), sg.Button("Volver", key="-VOLVER-")],
    ]


    columna_derecha = [
        [
            sg.Image(
                source=image_filename,
                key=("-AVATAR-"),
                size=(300, 300),
                subsample=3,
                pad=((125, 125), (0, 0)),
            )
        ],
        [
            sg.FileBrowse(
                "Seleccionar Imagen",
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
            window["-AVATAR-"].update(
                source=filename,
                size=(300, 300),
                subsample=3,
            )

        elif event == "-GUARDAR-":

            try:
                with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
                    perfiles = json.load(archivo)
            except (FileNotFoundError, PermissionError, json.JSONDecodeError):
                pass
            
            perfil_modificado = modificar_perfil(perfil_actual,values)

            for pos, perfil in enumerate(perfiles):
                if perfil['Usuario'] == perfil_modificado['Usuario']:      
                    perfiles[pos] = perfil_modificado
                    break
            
            with open(ruta_archivo, "w") as archivo:
                json.dump(perfiles, archivo, indent=4)
                print("Se modifico el perfil")

            window.close()
            return perfil_modificado
        
    return perfil_actual
        

if __name__ == "__main__":
    ventana_editar_perfil(menu_principal.perfil_actual)
