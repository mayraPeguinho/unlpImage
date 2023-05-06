import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pantallas import generador_memes
from pantallas import Generador_collage

def ventana_menu():

    layout = [[sg.Text(("Menu"),font=(40),justification="left")],
             [sg.Button(button_text= "Perfil"),sg.Button(button_text= "Configuracion"),sg.Button(button_text= '?',tooltip="Ayuda")],
             [sg.Button(button_text= "Etiquetar Imagenes")],
             [sg.Button(button_text= "Generar meme")],
             [sg.Button(button_text= "Generar collage")],
             [sg.Button(button_text= "Salir")]]
    return sg.Window("Menú principal",layout,margins=(200, 150))

def generar_ventana_de_ayuda(ventana):
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

menu=ventana_menu()

while True:
    evento, valores = menu.read()
    match evento:
        case sg.WIN_CLOSED:
            break
        case "Salir":
            break
        case "?":
            generar_ventana_de_ayuda(menu)
        case "Generar meme":
            menu.hide()
            if __name__ =="__main__":
                generador_memes.generar_meme()
            menu.un_hide() #esta linea dentro de la funcion generardor de memes en boton "Volver"
        case "Generar collage":
            menu.hide()
            if __name__ =="__main__":
                Generador_collage.generar_collage()
            menu.un_hide()
        case "Etiquetar imagenes":
            #mostrar etiquetar imagenes
            x=1
        case "Configuracion":
            #mostrar configuracion
            x=1
                 
menu.close()