import os
import PySimpleGUI as sg
from PIL import Image
import menu_principal
from funcionalidad.verificar_input import falta_completar_campos
from funcionalidad.nuevo_perfil import *

def ventana_nuevo_perfil():

    ruta_imagen = os.path.join(os.getcwd(), "imagenes", "imagenes_perfil", "avatar.png")

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
                file_types=(("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),),
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


    window = sg.Window("Nuevo perfil", layout,metadata=)

    while True:
        event, values = window.read()

        if event == "-VOLVER-" or event == sg.WIN_CLOSED:
            break

        elif event == "-BROWSE-":
            filename = values["-BROWSE-"]
            window["-AVATAR-"].update(
                source=filename,
                size=(300, 300),
                subsample=3,
            )

        elif event == "-GUARDAR-":
            if not falta_completar_campos(values):
                if not existe_nombre(values["-USUARIO-"]):
                    if verificar_edad(values["-EDAD-"]):
                        usuario_nuevo = crear_perfil(values)
                        perfil_json = crear_json(usuario_nuevo)

                        with open(ruta_archivo, "w") as archivo:
                            json.dump(perfil_json, archivo)
                            print("Se creo el perfil")

                        window.close()

                    else:
                        sg.popup("Ingresa una edad valida")
                else:
                    sg.popup("Usuario existente, ingrese otro nombre de usuario")
            else:
                sg.popup("Falta llenar el formulario")

    window.close()

if __name__ =="__main__":
    ventana_nuevo_perfil()