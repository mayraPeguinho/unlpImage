import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import generador_memes
from pantallas import Generador_collage

def generar_ventana_de_ayuda(ventana):
    '''Esta funcion define la ventana de ayuda
       donde se explica la funcionalidad de la aplicacion al usuario. '''
    
    layout = [[sg.Text("UNLPImage es una aplicación de escritorio que permite realizar memes o collages con imagenes almacenadas en el dispositivo.")],
              [sg.Button(button_text= "Volver")]]
    ventana_de_ayuda=sg.Window("Ayuda",layout,margins=(200, 150))
    ventana.hide()
    while True:
        evento, valores = ventana_de_ayuda.read()
        if evento == sg.WIN_CLOSED or evento=="Volver":
            ventana_de_ayuda.close()  
            ventana.un_hide()
            break

def ventana_menu():

    layout = [[sg.Text(("Menu"),font=("Helvetica",20),justification="left")],
             [sg.Button(button_text= "Perfil"),sg.Button(button_text= "Configuracion"),sg.Button(button_text= '?',tooltip="Ayuda")],
             [sg.Button(button_text= "Etiquetar Imagenes")],
             [sg.Button(button_text= "Generar meme")],
             [sg.Button(button_text= "Generar collage")],
             [sg.Button(button_text= "Salir")]]
    
    return sg.Window("UNLPImage",layout,margins=(150, 150),metadata=None)

if __name__ =="__main__":
    ventana_menu()
                 