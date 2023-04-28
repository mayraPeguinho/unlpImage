import PySimpleGUI as sg

def menu_window():
    layout = [[sg.Button(button_text= '?',tooltip="Ayuda")],
             [sg.Button(button_text= "Perfil")],
             [sg.Button(button_text= "Configuracion")],
             [sg.Button(button_text= "Etiquetar Imagenes")],
             [sg.Button(button_text= "Generar meme")],
             [sg.Button(button_text= "Generar collage")],
             [sg.Button(button_text= "Salir")]]
    return sg.Window("Menú principal",layout,margins=(200, 150))

def help_window():
    layout = [[sg.Text("Este es un mensaje de ayuda donde se explica la funcionalidad del programa")],
              [sg.Button(button_text= "Volver")]]
    return sg.Window("Ayuda",layout,margins=(200, 150))

window=menu_window()
window_help=help_window()

while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case "?":
            window.hide()
            while True:
                event, values = window_help.read()
                if event == sg.WIN_CLOSED:
                    window_help.close()  
                    window.close()
                    break
                if event== "Volver":
                    window_help.close()
                    window.un_hide()
                    break
                
window_help.close()  
window.close()

#Que hacemos si cierra ventana desde otra que no sea la de Inicio? Cerramos todo el programa?