import PySimpleGUI as sg
import os
import json
import sys

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
