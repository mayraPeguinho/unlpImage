def pantalla_configuracion(usuario):
    import PySimpleGUI as sg
    import sys
    import os



    # Obtengo la ruta del directorio padre de este archivo
    DIRECTORIO_PADRE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Agrego el directorio raiz a la ruta de búsqueda de módulos
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from funcionalidad import configuracion as conf 

    layout = [[sg.Text('Repositorio de imagenes')],
            # En este directorio se encuentran las imagenes que podemos utilizar en la aplicación
            [sg.Input(), sg.FolderBrowse(button_text="Seleccionar")],
            [sg.Text('Directorio de collages')],
            # En este directorio almacenaremos los collages
            [sg.Input(), sg.FolderBrowse(button_text="Seleccionar")],
            [sg.Text('Directorio de memes')],
            # En este directorio almacenaremos los memes
            [sg.Input(), sg.FolderBrowse(button_text="Seleccionar")],
            # Botones de guardar y volver
            [sg.OK(button_text="Guardar"), sg.Cancel(button_text="Volver")]]

    window = sg.Window("Configuración", layout, margins=(200, 150))

    #guardar usuario
    usuario_actual = usuario

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Volver':
            break
        if event == 'Guardar':
            # Obtengo la ruta absoluta de la carpeta seleccionada
            repo_imagenes = os.path.abspath(values[0])
            carpeta_collages = os.path.abspath(values[1])
            carpeta_memes = os.path.abspath(values[2])

            # Verifico que la carpeta seleccionada sea una subcarpeta del directorio padre
            if os.path.commonpath([DIRECTORIO_PADRE, repo_imagenes]) != DIRECTORIO_PADRE:
                sg.popup_error('La carpeta seleccionada debe estar dentro de {}'.format(DIRECTORIO_PADRE))
            else:
                conf.guardar_directorios(os.path.relpath(repo_imagenes, DIRECTORIO_PADRE),
                                    os.path.relpath(carpeta_collages, DIRECTORIO_PADRE),
                                    os.path.relpath(carpeta_memes, DIRECTORIO_PADRE), DIRECTORIO_PADRE, usuario_actual)
                sys.exit()

    window.close()

if __name__ =="__main__":
    pantalla_configuracion(usuario)