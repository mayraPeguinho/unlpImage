import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funcionalidad import configuracion as conf 
from rutas import directorio_padre

def pantalla_configuracion(usuario):
    '''Genera la pantalla de configuracion, con su layout y su manejador de eventos,
    recibiendo como parametro el usuario del perfil actual, para identificar quien
    realiza cambios en la configuracion
    '''
    repositorio_imagenes=conf.obtener_directorio('repositorio_imagenes')
    directorio_collage=conf.obtener_directorio('directorio_collages')
    directorio_meme=conf.obtener_directorio('directorio_memes')

    layout = [[sg.Text('Repositorio de imagenes')],
            # En este directorio se encuentran las imagenes que podemos utilizar en la aplicación
            [sg.Input(default_text=repositorio_imagenes), sg.FolderBrowse(button_text="Seleccionar")],
            [sg.Text('Directorio de collages')],
            # En este directorio almacenaremos los collages
            [sg.Input(default_text=directorio_collage), sg.FolderBrowse(button_text="Seleccionar")],
            [sg.Text('Directorio de memes')],
            # En este directorio almacenaremos los memes
            [sg.Input(default_text=directorio_meme), sg.FolderBrowse(button_text="Seleccionar")],
            # Botones de guardar y volver
            [sg.OK(button_text="Guardar"), sg.Cancel(button_text="Volver")]]

    window = sg.Window("Configuración", layout, margins=(200, 150))

    #guardar usuario
    usuario_actual = usuario

    while True:
        event, values = window.read()
        if event == 'Volver':
            window.close()
            break
        elif event == sg.WIN_CLOSED:
            sys.exit()
        if event == 'Guardar':
            repo_imagenes = os.path.join(values[0])
            carpeta_collages = os.path.join(values[1])
            carpeta_memes = os.path.join(values[2])

            # Verifico que la carpeta seleccionada sea una subcarpeta del directorio padre
            if os.path.commonpath([directorio_padre, repo_imagenes]) != directorio_padre:
                sg.popup_error('La carpeta seleccionada debe estar dentro de {}'.format(directorio_padre))
            else:
                conf.guardar_directorios(os.path.relpath(repo_imagenes, directorio_padre),
                                    os.path.relpath(carpeta_collages, directorio_padre),
                                    os.path.relpath(carpeta_memes, directorio_padre), directorio_padre, usuario_actual)
                sg.popup("La configuración se ha guardado correctamente")

if __name__ =="__main__":
    pantalla_configuracion("null")