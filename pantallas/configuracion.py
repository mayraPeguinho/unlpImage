import PySimpleGUI as sg
#from funcionalidad import congifuracion as cf 


#layout = [[sg.Input('Repositorio de imagenes')], [sg.Input('Directorio de collages')], 
#          [sg.Input('Repositorio de imagenes')]]

#sg.Window("Configuración", layout, margins=(200, 150)).read()

layout = [[sg.Text('Repositorio de imagenes')],
          [sg.Input(), sg.FolderBrowse(button_text= "Seleccionar")],
          [sg.Text('Directorio de collages')],
          [sg.Input(), sg.FolderBrowse(button_text= "Seleccionar")],
          [sg.Text('Directorio de memes')],
          [sg.Input(), sg.FolderBrowse(button_text= "Seleccionar")],
          [sg.OK(button_text="Guardar"), sg.Cancel(button_text="Volver")]]

window = sg.Window("Configuración", layout, margins=(200, 150)).read()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'OK':
        folder_path = values[0]
        print(f'Se seleccionó la carpeta: {folder_path}')

window.close()