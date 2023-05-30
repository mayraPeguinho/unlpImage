import PySimpleGUI as sg
import sys


def ventana_seleccion_collage():
    layout = [[sg.Text("Seleccion de Collage")],
              [sg.Button("Volver",key="-VOLVER-")]
             ]
            #Agregar botones para los cuatro diseños de collage minimos
    
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


