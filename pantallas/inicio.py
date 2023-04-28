import PySimpleGUI as sg

def first_window():
    layout = [[sg.Button(button_text= "+")],
              [sg.Button(button_text= "Ver más")]]
    return sg.Window("UNLPImage",layout,margins=(200, 150))

window=first_window()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
        
window.close()