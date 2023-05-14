import sys
import os
import json
import PySimpleGUI as sg
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from pantallas import menu_principal

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

def modifcar_perfil(perfil):
    pass



window = sg.Window("Editar perfil", layout)

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
            size=(60, 60),
        )

    elif event == "-GUARDAR-":
        
        perfil_modificado = modifcar_perfil(perfil)
        with open(ruta_archivo, "w") as archivo:
            json.dump(values, archivo)
            print("Se modifico el perfil")
        #return perfil_modificado (para cuando se haga funcion)
