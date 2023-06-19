import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pantallas import generador_collage
from rutas import ruta_diseños_collages

def ventana_seleccion_collage():
    '''Crea el layout de la ventana de seleccion de collage, consta de los botones para
    los posibles diseños de la aplicacion
    '''
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
    return sg.Window("Generar Collage",layout,margins=(150, 150))

def eventos_seleccion_collage(usuario):
    '''Maneja los eventos de la ventana de seleccion de collage
    Los botones que son imagenes, invocan la pantalla de generar_collage
    '''
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
                ventana.hide()
                generador_collage.generar_collage(usuario,2,1)
                ventana.un_hide()
            case "-DISEÑO 2-":
                ventana.hide()
                generador_collage.generar_collage(usuario,3,2)
                ventana.un_hide()
            case "-DISEÑO 3-":
                ventana.hide()
                generador_collage.generar_collage(usuario,4,3)
                ventana.un_hide()
            case "-DISEÑO 4-":
                ventana.hide()
                generador_collage.generar_collage(usuario,2,4)
                ventana.un_hide()
                
if __name__ =="__main__":
     eventos_seleccion_collage("usuario")


