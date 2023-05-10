import sys
import os
import json
import PySimpleGUI as sg
from PIL import Image

ruta_imagen = os.path.join(os.getcwd(), "imagenes", "imagenes_perfil", "avatar.png")

ruta_archivo = os.path.join(os.getcwd(), "datos", "perfil_nuevo.json")

extensiones_incluidas = ['jpg', 'jpeg', 'png', 'gif']
nombres_archivos = [fn for fn in os.listdir(os.path.join(os.getcwd(), 'imagenes'))
                    if any(fn.endswith(ext) for ext in extensiones_incluidas)]

columna_izquierda = [
    [sg.Text("Nuevo perfil")],
    [sg.Text("Usuario:")],
    [sg.InputText(key="-USUARIO-")],
    [sg.Text("Nombre:")],
    [sg.InputText(key="-NOMBRE-")],
    [sg.Text("Edad:")],
    [sg.InputText(key="-EDAD-", size=(10,))],
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

window = sg.Window("Nuevo perfil", layout)


def verificar_edad(edad):
    """Chequea que la edad ingresada sea un numero entero entre 0-99"""

    try:
        int(edad)
        return (edad < 0) or (edad > 99)
    except (TypeError, ValueError):
        return False


"""
def existe_nombre(alias):
    '''Chequea si ya existe el alias en el archivo JSON.'''
    x = True
    try:
        with open(ruta_archivo, 'r', encoding="UTF-8") as archivo:
            datos_perfil = json.load(archivo)     
            x = True if alias in datos_perfil else False
    except (FileNotFoundError, PermissionError):
        x = False
    return x 
"""


def existe_nombre(alias):
    """Chequea si ya existe el alias en el archivo JSON."""

    try:
        with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
            datos_perfil = json.load(archivo)

    except (FileNotFoundError, PermissionError):
        return False

    return True if alias in datos_perfil else False



def crear_usuario(usuario):
    with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
        datos_agregar = json.load(archivo)

    datos_agregar.append(usuario)



while True:
    event, values = window.read()

    if event == "-VOLVER-" or event == sg.WIN_CLOSED:
        break

    elif event == "-BROWSE-":
        filename = values["-BROWSE-"]
        window["-AVATAR-"].update(
            source=filename,
            size=(300,300),
            subsample=3,
        )

    elif event == "-GUARDAR-":
        if not existe_nombre(values["-USUARIO-"]):
            if verificar_edad(values["-EDAD-"]):
                # valores = usuario(values)
                # hacer una lista vacía, a medida que agregas perfiles abris el json, lo pasas a lista, editas esa lista y escribis
                usuario_nuevo = crear_usuario(values)  # tomas los valores ingresados de values y llamas a alguna funcion que te cree el usuario
                # guardar usuario_nuevo en el archivo JSON de usuarios
                with open(ruta_archivo, "w") as archivo:
                    json.dump(usuario_nuevo, archivo)
                    print("Se creo el perfil")
                
                window.close()

            else:
                sg.popup("Ingresa una edad valida")
        else:
            sg.popup("Usuario existente, ingrese otro nombre de usuario")

window.close()
