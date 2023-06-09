import os
import sys
import PySimpleGUI as sg
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcionalidad.verificar_input import falta_completar_campos
from funcionalidad.nuevo_perfil import *
from pantallas import menu_principal
from pantallas import inicio
import rutas as r


def ventana_nuevo_perfil():

    ruta_archivo=r.archivo_perfiles_json
    ruta_avatares= os.path.join(r.ruta_imagenes_perfil,'avatar.png')

    columna_izquierda = [
        [sg.Text("Nuevo perfil")],
        [sg.Text("Usuario:")],
        [sg.InputText(key="Usuario")],
        [sg.Text("Nombre:")],
        [sg.InputText(key="Nombre")],
        [sg.Text("Edad:")],
        [sg.InputText(key="Edad", size=(10,))],
        [sg.Text("Genero:")],
        [
            sg.Listbox(
                ['Masculino','Femenino','Otro'],
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
                source=ruta_avatares,
                key=("Avatar"),
                size=(300, 300),
                subsample=3,
                pad=((125, 125), (0, 0)),
            )
        ],
        [
            sg.FileBrowse(
                "Seleccionar Imagen",
                key=("-BROWSE-"),
                change_submits=True,
                enable_events=True,
                #file_types=(("Archivo de tipos", "*.png;*.jpg;*.jpeg;*.gif"),),
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


    window = sg.Window("Nuevo perfil", layout,metadata={"perfil_actual":None})

    while True:
        event, values = window.read()

        if event == "-VOLVER-":
            window.close()
            inicio.eventos_inicio()
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
                llenar_solo(values)
                if not falta_completar_campos(values):
                    if not existe_nombre(values["Usuario"]):
                        if verificar_edad(values["Edad"]):
                            usuario_nuevo = crear_perfil(values)

                            perfil_json = crear_json(usuario_nuevo)
                            try:
                                with open(ruta_archivo, "w") as archivo:
                                    json.dump(perfil_json, archivo,indent=4)
                            except (FileNotFoundError, PermissionError, json.JSONDecodeError):
                                pass

                            sg.popup('Se creo el perfil!')
                            window.close()
                            menu=menu_principal.ventana_menu(usuario_nuevo)
                            menu_principal.eventos_menu_principal(menu)

                        else:
                            sg.popup("Ingresa una edad valida")
                    else:
                        sg.popup("Usuario existente, ingrese otro nombre de usuario")
                else:
                    sg.popup("Falta llenar el formulario")


    window.close()


if __name__ == "__main__":
    ventana_nuevo_perfil()
