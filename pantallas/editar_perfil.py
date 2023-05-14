import sys
import os
import json
import PySimpleGUI as sg
from PIL import Image

ruta_imagen = os.path.join(os.getcwd(), "imagenes", "imagenes_perfil", "avatar.png")

ruta_archivo = os.path.join(os.getcwd(), "datos", "perfil_nuevo.json")

columna_izquierda = [
    [sg.Text("Editar perfil")],
    [sg.Text("Nombre:")],
    [sg.InputText(key="-NOMBRE-")],
    [sg.Text("Edad:")],
    [sg.Input(key="-EDAD-", size=(10,))],
    [sg.Text("Genero:")],
    [
        sg.Listbox(
            ["Masculino", "Femenino", "Otro"],
            no_scrollbar=False,
            s=(15, 3),
            key="-GENERO-",
        )
    ],
    [sg.Text("Especificar genero:")],
    [sg.InputText(key="-ESPECIFICAR_GENERO-")],
    [sg.Button("Guardar", key="-GUARDAR-"), sg.Button("Volver", key="-VOLVER-")],
]


columna_derecha = [
    [
        sg.Image(
            source=ruta_imagen,
            key=("-AVATAR-"),
            size=(60, 60),
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

def mostrar_perfil(perfil_actual):
    """ Guardo los valores del perfil"""

    perfil = {
        "Nombre": perfil_actual["-NOMBRE-"],
        "Edad": perfil_actual["-EDAD-"],
        "Genero": perfil_actual["-GENERO-"],
        "Especificar genero": perfil_actual["-ESPECIFICAR_GENERO-"],
        "Avatar": perfil_actual["-BROWSE-"],
    }
    return perfil

def modificar_perfil(perfil_actual, cambios_perfil):
    cambios_perfil = {
        perfil_actual['-NOMBRE-']: cambios_perfil['-NOMBRE-'],
        perfil_actual['-EDAD-']: cambios_perfil['-EDAD-'],
        perfil_actual['-GENERO-']: cambios_perfil['-GENERO-'],
        perfil_actual['-ESPECIFICAR_GENERO-']: cambios_perfil['-ESPECIFICAR_GENERO-'],
        perfil_actual['-BROWSE-']: os.path.basename(cambios_perfil['-BROWSE-']),
    }
    return cambios_perfil

window = sg.Window("Editar perfil", layout)

while True:
    event, values = window.read()

    mostrar_perfil(perfil_actual)

    if event == "-VOLVER-" or event == sg.WIN_CLOSED:
        break


    elif event == "-BROWSE-":
        filename = values["-BROWSE-"]
        window["-AVATAR-"].update(
            source=filename,
            size=(60, 60),
        )

    elif event == "-GUARDAR-":
        
        perfil_modificado = modifcar_perfil(perfil_actual,values)

        with open(ruta_archivo, "w") as archivo:
            json.dump(perfil_modificado, archivo, indent=4)
            print("Se modifico el perfil")

window.close()
