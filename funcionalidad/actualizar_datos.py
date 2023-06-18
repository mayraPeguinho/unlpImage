import PySimpleGUI as sg
from PIL import Image, ImageTk
import os
import json
import sys
import io

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import rutas as r

def actulizar_data():
    '''Retorna los datos de los diferentes perfiles almacenados en nuevo_perfil.json
    y los indices para cada uno de estos perfiles que posteriormente se usaran
    como la llave del evento. En caso de que el archivo este vacio o no exista,
    retorna listas vacias, en caso de no tener permisos, la app no se inicializa
    '''
    try:
        with open(r.archivo_perfiles_json,"r",encoding="UTF-8") as archivo:
            data = json.load(archivo)
        keys=list(map(lambda i: i, range(data.__len__())))
        return data,keys
    except (FileNotFoundError,json.JSONDecodeError):
        data=[]
        keys=[]
        return data,keys
    except PermissionError:
        sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'nuevo_perfil.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
        sys.exit()

def mostrar_imagen(ruta):
    '''Esta funcion reajusta la imagen de perfil de un determinado usuario
    y retorna la variable image_bytes que posee el valor que PySimpleGui puede
    leer.
    '''
    imagen = Image.open(ruta)
    new_size=(80,80)
    imagen_redimensionada = imagen.resize(new_size)
    with io.BytesIO() as output:
        imagen_redimensionada.save(output, format='PNG')
        image_bytes = output.getvalue()
    return image_bytes


