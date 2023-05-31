import PySimpleGUI as sg
from PIL import Image, ImageTk
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#from rutas import archivo_imagenes_etiquetadas_csv as ruta_archivo
from rutas import ruta_repositorio_imagenes as ruta_archivo_def
from funcionalidad.verificar_input import falta_completar_campos
def layout(cant_imagenes):
    imagenes = [imag for imag in os.listdir(ruta_archivo_def) if imag.endswith((".jpg", ".jpeg", ".png"))]
    column1 = [
        [sg.Text("Seleccionar imagenes")],
    ]
    column1.extend([[sg.Combo(imagenes, key=f"-IMAGEN-{i+1}-")] for i in range(cant_imagenes)])
    column1.append([sg.Button("Actualizar", key="-ACTUALIZAR-")])

    column2 = [
         [sg.Image(key="-IMAGEN-", size=(400, 400))],
         [sg.Column(
         [[sg.Button("Guardar", key="-GUARDAR-")]],
                     expand_x=True,
                     element_justification="right"
                   )
         ],
    ]

    return [
        [   [sg.Text("Generar Collage", font=("Helvetica", 20), justification="left"),
             sg.Column( [[sg.Button("Volver", key="-VOLVER-")]],
                          expand_x=True,
                          element_justification="right"
                      )
           ],
        
            sg.Column(column1,vertical_alignment="center"),
            sg.Column(column2,vertical_alignment="center"),
        ]
    ]
def generar_collage(cant_imagenes):
     
     window = sg.Window("Generador de Collages", layout(cant_imagenes),margins=(60,30))
     while True:
         evento, valores = window.read()
         if evento == "-VOLVER-":
             window.close()
             break
         elif evento == sg.WIN_CLOSED:
             sys.exit()
         elif evento == "-GUARDAR-":
             if falta_completar_campos(valores):
                 sg.popup("Falta completar los campos necesarios")
                   
             else:
                 #funcion para crear un collage
                 sg.popup("Se genero un nuevo collage!")
                 break
         elif evento== "-ACTUALIZAR-":
             pass
     window.close()


if __name__ =="__main__":
     #Le paso la cantidad de imagenes que tendrá el collage
     generar_collage(6)


    