import os
import sys
import json

def actulizar_data():
    '''Retorna los datos de los diferentes perfiles almacenados en nuevo_perfil.json
        y los indices para cada uno de estos perfiles que posteriormente se usaran
        como la llave del evento
    '''
    archivo_perfiles_json = os.path.join(os.getcwd(),'datos', 'nuevo_perfil.json')
    try:
        with open(archivo_perfiles_json,"r",encoding="UTF-8") as archivo:
            data = json.load(archivo)
        keys=list(map(lambda i: i, range(data.__len__())))
    except (FileNotFoundError,PermissionError,json.JSONDecodeError):
        data=[]
    return data,keys