import PySimpleGUI as sg
from PIL import Image, ImageTk
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rutas import ruta_repositorio_imagenes as ruta_archivo_def
from funcionalidad.verificar_input import falta_completar_campos
from rutas import ruta_diseños_collages

def layout(cant_imagenes):

    imagenes = [imagen for imagen in os.listdir(ruta_archivo_def) if imagen.endswith((".jpg", ".jpeg", ".png"))]
    column1 = [
        [sg.Text("Seleccionar imagenes")],
    ]
    column1.extend([[sg.Combo(imagenes, key=f"-IMAGEN-{i+1}-")] for i in range(cant_imagenes)])
    column1.append([sg.Text("Título")])
    column1.append([sg.Input(key="-TÍTULO-",size=(35))])
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


def generar_collage(diseño,cant_imagenes):
     
     window = sg.Window("Generador de Collages", layout(cant_imagenes),margins=(60,30),element_justification="center",resizable=True)
     window.finalize()
     
     #muestro el diseño del collage elegido
     path_collage=os.path.join(ruta_diseños_collages, diseño)
     collage= Image.open(path_collage)
     
     imagen = ImageTk.PhotoImage(collage)
     window["-IMAGEN-"].update(data=imagen)

     

     while True:
         evento, valores = window.read()
         if evento == "-VOLVER-":
             window.close()
             break
         elif evento == sg.WIN_CLOSED:
             sys.exit()
         elif evento == "-ACTUALIZAR-":
                 #inicializo la lista por si seleccioné otras imagenes
                 images=[]
                 
                 #obtengo la lista de imagenes con las que voy a crear el collage
                 for i in range(cant_imagenes):
                     image_path = os.path.join(ruta_archivo_def, valores[f"-IMAGEN-{i+1}-"])
                     image = Image.open(image_path)
                     images.append(image)

                 #muestro el collage altualizado
                 imagen_actualizada = ImageTk.PhotoImage(collage)
                 window["-IMAGEN-"].update(data=imagen_actualizada)


         elif evento == "-GUARDAR-":
             if not falta_completar_campos(valores):
                 #Guardo el collage
                 sg.popup("El collage se generó con éxito")
                 break
             else:
                  sg.popup("Falta completar los campos necesarios")
           
     window.close()


if __name__ =="__main__":
     #diseño seleccionado
     diseño = 'collage_3.png'
     #cantidad de imagenes que tendrá el collage
     cant_imagenes = 4
     generar_collage(diseño, cant_imagenes)

    