import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from funcionalidad.verificar_input import falta_completar_campos

def generar_collage():
     '''Esta funcion define una ventana 
       para generar collages a partir de imágenes y plantillas seleccionadas por el usuario. '''
     layout = [
    [
        sg.Text("Generar Collage", font=("Helvetica", 20), justification="left"),
        sg.Column(
            [[sg.Button("Volver ➡", key="-VOLVER-")]],
            expand_x=True,
            element_justification="right"
        ),
     ],
     [sg.Text("Seleccionar imágenes")],
    [sg.Input(), sg.FilesBrowse("Seleccionar Imagenes",key="-FILES-",file_types=(("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),),files_delimiter=";",)],
     [sg.Text("Seleccionar plantilla")],
     [sg.Combo(["Plantilla 1", "Plantilla 2", "Plantilla 3", "Plantilla 4", "Plantilla 5"], key="Listar Plantillas")],
     [sg.Column([[sg.Button("Generar Collage", key="-GENERAR COLLAGE-")]], expand_x=True, element_justification="right")],
     ]

     window = sg.Window('Generador de collage', layout, margins=(60, 80), finalize=True, resizable=True)

     while True:
         evento, valores = window.read()
         if evento == "-VOLVER-":
             window.close()
             break
         elif evento == sg.WIN_CLOSED:
             sys.exit()
         elif evento == "-GENERAR COLLAGE-":
             if falta_completar_campos(valores):
                 sg.popup("Falta completar los campos necesarios")
                   
             else:
                 #funcion para crear un collage
                 sg.popup("Se genero un nuevo collage!")
                 break


if __name__ =="__main__":
     generar_collage()


    