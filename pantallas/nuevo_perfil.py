import os
import sys

import PySimpleGUI as sg
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from funcionalidad.verificar_input import falta_completar_campos
from funcionalidad.nuevo_perfil import *
from funcionalidad import registrar_log
from pantallas import menu_principal
from pantallas import inicio
import rutas as r


def ventana_nuevo_perfil():
    '''Genera la ventana de nuevo perfil, tanto su layout como se manejador
    de eventos
    '''

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
                ['Masculino','Femenino','Otro'],
                no_scrollbar=False,
                s=(15, 3),
                key="-GENERO-",
                enable_events=True,
            )
        ],
        [sg.Text("Especificar genero:")],
        [sg.InputText(key="-ESPECIFICAR_GENERO-", disabled=True)],
        [sg.Button("Guardar", key="-GUARDAR-"), sg.Button("Volver", key="-VOLVER-")],
    ]

    columna_derecha = [
        [
            sg.Image(
                source=r.ruta_imagen_por_defecto,
                key=("-AVATAR-"),
                size=(300, 300),
                subsample=3,
                pad=((125, 125), (0, 0)),
            )
        ],
        [
            sg.FileBrowse(
                "Seleccionar Imagen",
                initial_folder=r.ruta_imagenes_perfil,
                key=("-BROWSE-"),
                change_submits=True,
                enable_events=True,
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
            window["-AVATAR-"].update(filename,
            size=(300, 300),
            subsample=3,
            )
        
        elif event == "-GENERO-":
            genero = values["-GENERO-"][0]
            if genero == "Otro":
                window["-ESPECIFICAR_GENERO-"].update(disabled=False)
            else:
                window["-ESPECIFICAR_GENERO-"].update(disabled=True)

        elif event == "-GUARDAR-":
                llenar_solo(values)
                if not falta_completar_campos(values):
                    if not existe_nombre(values["-USUARIO-"]):
                        if verificar_edad(values["-EDAD-"]):
                            usuario_nuevo = crear_perfil(values)

                            perfil_json = crear_json(usuario_nuevo)
                            try:
                                with open(ruta_archivo, "w") as archivo:
                                    json.dump(perfil_json, archivo,indent=4)
                            except (PermissionError):
                                sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'nuevo_perfil.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
                                sys.exit()
                            except(FileNotFoundError):
                                sg.popup("No se encontro el archivo nuevo_perfil.json")
                                sys.exit()
                            except(json.JSONDecodeError):
                                sg.popup("Error fatal: Faltan archivos importante, el programa se cerrará")
                                sys.exit()
                            
                            registrar_log.registrar_interaccion(values['-USUARIO-'],"Nuevo usuario")
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

