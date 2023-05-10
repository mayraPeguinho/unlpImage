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
        return 99 > int(edad) > 0
    except (TypeError, ValueError):
        return False


def existe_nombre(alias):
    '''Chequea si ya existe el alias en el archivo JSON.'''
    try:
        with open(ruta_archivo, 'r', encoding="UTF-8") as archivo:
            datos_perfil = json.load(archivo)

        for nombre_usuario in datos_perfil:
            if nombre_usuario['-USUARIO-'] == alias:
                return True

    except (FileNotFoundError, PermissionError, json.JSONDecodeError):
        return False


def crear_usuario(usuario):
    '''Le paso el usuario y lo agregar al archivo JSON'''
    datos_agregar= []
    try:
        with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
            datos_agregar = json.load(archivo)
    except(FileNotFoundError,PermissionError,json.JSONDecodeError):
        pass 
    datos_agregar.append(usuario)
    return datos_agregar


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
                usuario_nuevo = crear_usuario(values) 
                    
                with open(ruta_archivo, "w") as archivo:
                    json.dump(usuario_nuevo, archivo)
                    print("Se creo el perfil")
                    
                window.close()

            else:
                sg.popup("Ingresa una edad valida")
        else:
            sg.popup("Usuario existente, ingrese otro nombre de usuario")

window.close()
