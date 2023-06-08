import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pantallas import generador_collage
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

def eventos_seleccion_collage():
    ventana=ventana_seleccion_collage()
    while True:
        evento, valores = ventana.read()
        match evento:
            case sg.WIN_CLOSED:
                sys.exit()
            case "-VOLVER-":
                ventana.close()
                break
            case "-DISEÑO 1-":
                ventana.metadata["cantidad_imagenes"]=2
                ventana.hide()
                generador_collage.generar_collage('collage_1.png',2)
                ventana.un_hide()
            case "-DISEÑO 2-":
                ventana.metadata["cantidad_imagenes"]=2
                ventana.hide()
                generador_collage.generar_collage(2)
                ventana.un_hide()
            case "-DISEÑO 3-":
                ventana.metadata["cantidad_imagenes"]=3
                ventana.hide()
                generador_collage.generar_collage(3)
                ventana.un_hide()
            case "-DISEÑO 4-":
                ventana.metadata["cantidad_imagenes"]=4
                ventana.hide()
                generador_collage.generar_collage(4)
                ventana.un_hide()


if __name__ =="__main__":
     eventos_seleccion_collage()


