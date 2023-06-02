import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rutas import ruta_diseños_collages

def ventana_seleccion_collage():
    layout = [[sg.Text("Seleccion de Collage")],
              [sg.Button(image_source=os.path.join(ruta_diseños_collages,'collage_1.png'),
                        image_size=(147,159),
                        image_subsample=3,
                        key="-DISEÑO 1-"),
               sg.Button(image_source=os.path.join(ruta_diseños_collages,'collage_2.png'),
                        image_size=(147,159),
                        image_subsample=3,
                        key="-DISEÑO 2-"),
                sg.Button(image_source=os.path.join(ruta_diseños_collages,'collage_3.png'),
                        image_size=(147,159),
                        image_subsample=3,
                        key="-DISEÑO 3-"),
                sg.Button(image_source=os.path.join(ruta_diseños_collages,'collage_4.png'),
                        image_size=(147,159),
                        image_subsample=3,
                        key="-DISEÑO 4-")],
              [sg.Button("Volver",key="-VOLVER-")],
             ]
    return sg.Window("UNLPImage",layout,margins=(150, 150),metadata={"cantidad_imagenes":None})

def eventos_seleccion_collage(ventana_seleccion_collage):
    while True:
        evento, valores = ventana_seleccion_collage.read()
        match evento:
            case sg.WIN_CLOSED:
                sys.exit()
            case "-VOLVER-":
                ventana_seleccion_collage.close()
                break
            case "-DISEÑO 1-":
                ventana_seleccion_collage.metadata["cantidad_imagenes"]=2
                pass
            case "-DISEÑO 2-":
                ventana_seleccion_collage.metadata["cantidad_imagenes"]=2
                pass
            case "-DISEÑO 3-":
                ventana_seleccion_collage.metadata["cantidad_imagenes"]=3
                pass
            case "-DISEÑO 4-":
                ventana_seleccion_collage.metadata["cantidad_imagenes"]=4
                pass

eventos_seleccion_collage(ventana_seleccion_collage())


