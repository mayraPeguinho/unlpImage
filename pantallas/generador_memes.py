import PySimpleGUI as sg
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad.verificar_input import falta_completar_campos



def generar_meme(ruta_template):
     '''Esta funcion define una ventana 
     para generar memes a partir de una imágen y un seleccionados por el usuario. '''
     layout = [
             [ sg.Text("Generar Meme", font=("Helvetica", 20), justification="left"),
             sg.Column([[sg.Button("Volver ➡", key="-VOLVER-")]],expand_x=True,element_justification="right"),],
             [sg.Text('Seleccionar imagen:')],
             [sg.Input(), sg.FileBrowse("Seleccionar Imagen",file_types=(("Image Files", "*.png;*.jpg;*.jpeg;*.gif"),))],
             [sg.Text('Introducir el texto:')],
             [sg.InputText()],
             [sg.Column([[sg.Button("Generar", key="-GENERAR-")]], expand_x=True, element_justification="right")],

            
           ]
     window = sg.Window('Generador de memes',layout, margins=(60, 80), finalize=True, resizable=True)

     while True:
         evento, valores = window.Read()
         if evento == "-GENERAR-" :
             if not falta_completar_campos(valores) :  
                 #genero el meme
                 sg.popup("Se generó un meme!")
                 break
             else:
                 sg.popup("No se completaron los campos necesarios")
         elif evento == "-VOLVER-":
             window.close()
             break
         elif evento== sg.WIN_CLOSED:
             sys.exit()

if __name__ =="__main__":
     generar_meme()
  