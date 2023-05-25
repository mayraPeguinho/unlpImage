import os
import json
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rutas as r

def actulizar_data():
    '''Retorna los datos de los diferentes perfiles almacenados en nuevo_perfil.json
        y los indices para cada uno de estos perfiles que posteriormente se usaran
        como la llave del evento
    '''
    try:
        with open(r.archivo_perfiles_json,"r",encoding="UTF-8") as archivo:
            data = json.load(archivo)
        keys=list(map(lambda i: i, range(data.__len__())))
    except (FileNotFoundError,PermissionError,json.JSONDecodeError):
        data=[]
        keys=[]
    return data,keys