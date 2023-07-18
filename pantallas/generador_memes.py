import PySimpleGUI as sg
import sys
import os
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from funcionalidad.verificar_input import falta_completar_campos
import rutas as r
from funcionalidad import crear_meme
from funcionalidad import etiquetar_imagenes
from funcionalidad.crear_collage import es_nombre_valido
import PIL.ImageFont

def definir_layout(cant_cajas):
    """Se arma de que manera puede ser la interfaz dependiendo la cantidad
    de cajas de texto se tiene"""

    
    if cant_cajas == 1:
        columna_izquierda = [
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-', initial_folder=r.ruta_directorio_fuentes)],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Button("Actualizar", key="-ACTUALIZAR-"), sg.Button('Volver', key= '-VOLVER-')],
        ]
    elif cant_cajas == 2:
        columna_izquierda = [
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-', initial_folder=r.ruta_directorio_fuentes)],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Text('Texto 2:')],[sg.Input(key = '-TEXTO_2-')],
            [sg.Button("Actualizar", key="-ACTUALIZAR-"),sg.Button('Volver', key= '-VOLVER-')],
        ]
    elif cant_cajas == 3:
        columna_izquierda = [
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-', initial_folder=r.ruta_directorio_fuentes)],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Text('Texto 2:')],[sg.Input(key = '-TEXTO_2-')],
            [sg.Text('Texto 3:')],[sg.Input(key = '-TEXTO_3-')],
            [sg.Button("Actualizar", key="-ACTUALIZAR-"),sg.Button('Volver', key= '-VOLVER-')],
        ]
    elif cant_cajas == 4:
        columna_izquierda = [
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-',initial_folder=r.ruta_directorio_fuentes)],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Text('Texto 2:')],[sg.Input(key = '-TEXTO_2-')],
            [sg.Text('Texto 3:')],[sg.Input(key = '-TEXTO_3-')],
            [sg.Text('Texto 4:')],[sg.Input(key = '-TEXTO_4-')],
            [sg.Button("Actualizar", key="-ACTUALIZAR-"),sg.Button('Volver', key= '-VOLVER-')],
        ]
    elif cant_cajas == 5:
        columna_izquierda = [
            [sg.FileBrowse('Seleccionar fuente', key='-FUENTE-',initial_folder=r.ruta_directorio_fuentes)],
            [sg.Text('Texto 1:')],[sg.Input(key = '-TEXTO_1-')],
            [sg.Text('Texto 2:')],[sg.Input(key = '-TEXTO_2-')],
            [sg.Text('Texto 3:')],[sg.Input(key = '-TEXTO_3-')],
            [sg.Text('Texto 4:')],[sg.Input(key = '-TEXTO_4-')],
            [sg.Text('Texto 5:')],[sg.Input(key = '-TEXTO_5-')],
            [sg.Button("Actualizar", key="-ACTUALIZAR-"), sg.Button('Volver', key= '-VOLVER-')],
        ]

    columna_derecha = [
        [sg.Image(key="-IMAGEN-", size=(200, 200))],
        [
            sg.Column(
                [[sg.Button("Generar meme", key="-GENERAR-")]],
                expand_x=True,
                element_justification="right",
            )
        ],
    ]

    layout = [
        [
            sg.Column(columna_izquierda, element_justification="c"),
            sg.VSeperator(),
            sg.Column(columna_derecha, element_justification="c"),
        ]
    ]

    return layout


def generar_meme(imagen_seleccionada,meme_json,usuario):
    """Genera la interfaz gráfica para crear un meme con su manejador de eventos.
    Recibe el template seleccionado, el json de templates (en este se busca los datos
    del template especificado) y el usuario.
    """
    meme_json = [item for item in meme_json if item['image'] == os.path.basename(imagen_seleccionada)]

    cant_cajas = (meme_json[0]['text_boxes'].__len__())

    nombre_imagen = os.path.basename(imagen_seleccionada)

    layout = definir_layout(cant_cajas)

    window = sg.Window(
        "Generador de memes", layout, margins=(60, 80), finalize=True, resizable=True
    )
    """Muestro el meme que se me pasa por parametro"""

    cargar_meme = PIL.Image.open(imagen_seleccionada)
    imagen_meme = etiquetar_imagenes.mostrar_imagen(imagen_seleccionada)

    window["-IMAGEN-"].update(data=imagen_meme)


    while True:
        event, values = window.Read()

        window
        if event == "-VOLVER-":
            window.close()
            break

        elif event == sg.WIN_CLOSED:
            sys.exit()

        elif event == "-ACTUALIZAR-":
            meme_actual = crear_meme.actualizar_datos(cargar_meme,meme_json,values)

            cambio_tamanio = meme_actual.resize((350,300))

            data_imagen = PIL.ImageTk.PhotoImage(cambio_tamanio)
            window["-IMAGEN-"].update(data=data_imagen)

        elif event == "-GENERAR-":
            crear_meme.asigno_fuente(values)
            if not falta_completar_campos(values):
                nombre = sg.popup_get_text("Ingrese un nombre para el meme")
                if nombre is not None and es_nombre_valido(nombre) and nombre != '':
                    if (crear_meme.formato(nombre)):
                        crear_meme.guardar_meme(usuario,nombre,nombre_imagen,values,meme_actual)
                        sg.popup("Se generó un meme!")
                        window.close()
                        break
                    else:
                        sg.popup('Debe ingresar la extension de la imagen que desea(.jpg o .png)')
                else:
                    sg.popup("Ya existe un archivo con ese nombre. Por favor, ingrese otro nombre")
            else:
                sg.popup("No se completaron los campos necesarios")


if __name__ == "__main__":
    generar_meme()
    