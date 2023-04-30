import PySimpleGUI as sg
from generador_memes import generar_meme

def ventana_menu():
    layout = [[sg.Button(button_text= "Perfil"),sg.Button(button_text= "Configuracion"),sg.Button(button_text= '?',tooltip="Ayuda")],
             [sg.Button(button_text= "Etiquetar Imagenes")],
             [sg.Button(button_text= "Generar meme")],
             [sg.Button(button_text= "Generar collage")],
             [sg.Button(button_text= "Salir")]]
    return sg.Window("Menú principal",layout,margins=(200, 150))

def generar_ventana_de_ayuda(ventana):
    layout = [[sg.Text("Este es un mensaje de ayuda donde se explica la funcionalidad del programa")],
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
        case "Generador meme":
            #mostrar generador de memes
            menu.hide()
            generar_meme() #aca quiero usar la funcion y no puedo
        case "Generador collage":
            #mostrar generador de collage
            x=1
        case "Etiquetar imagenes":
            #mostrar etiquetar imagenes
            x=1
        case "configuracion":
            #mostrar configuracion
            x=1
                 
menu.close()

#Que hacemos si cierra ventana desde otra que no sea la de Inicio? Cerramos todo el programa?

#Con el boton salir tambien cierro el programa?

#Si importo otro archivo.py como generador_memes o cualquier otro me lo ejecuta de primero
#no me deja usar la funcion