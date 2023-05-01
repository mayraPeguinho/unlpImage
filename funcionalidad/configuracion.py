import json
import sys
import os

#Agrego el directorio raiz a la ruta de búsqueda de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def guardar_directorios(repositorio_imagenes, directorio_collages, directorio_memes):
    data = {'repositorio_imagenes': repositorio_imagenes,
            'directorio_collages': directorio_collages,
            'directorio_memes': directorio_memes}
    with open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos')), 'configuracion.json'), 'w') as archivo:
        json.dump(data, archivo)
        archivo.close()
