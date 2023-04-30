import PySimpleGUI as sg

def generar_ventana_de_inicio():
    layout = [[sg.Button(button_text= "+")],
              [sg.Button(button_text= "Ver más")]]
    return sg.Window("UNLPImage",layout,margins=(200, 150))

window=generar_ventana_de_inicio()

while True:
    evento, valores = window.read()
    match evento:
        case sg.WIN_CLOSED:
            break
        case "+":
            #Va la pestaña de nuevo perfil
            x=1
        case "ver mas":
            #muestra los demas perfiles
            x=1
        
window.close()