import PySimpleGUI as sg
import sys
import os

# Agrego el directorio raiz a la ruta de búsqueda de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funcionalidad.configuracion import guardar_directorios

layout = [[sg.Text('Repositorio de imagenes')],
          #En este directorio se encuentran las imagenes que podemos utilizar en la aplicación
          [sg.Input(), sg.FolderBrowse(button_text= "Seleccionar")],
          [sg.Text('Directorio de collages')],
          #En este directorio almacenaremos los collages
          [sg.Input(), sg.FolderBrowse(button_text= "Seleccionar")],
          [sg.Text('Directorio de memes')],
          #En este directorio almacenaremos los memes
          [sg.Input(), sg.FolderBrowse(button_text= "Seleccionar")],
          #Botones de guardar y volver
          [sg.OK(button_text="Guardar"), sg.Cancel(button_text="Volver")]]

window = sg.Window("Configuración", layout, margins=(200, 150))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Volver':
        break
    if event == 'Guardar':
        repo_imagenes = values[0]
        carpeta_collages = values[1]
        carpeta_memes = values[2]
        guardar_directorios(repo_imagenes, carpeta_collages, carpeta_memes)
        sys.exit()
window.close()