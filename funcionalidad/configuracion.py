import json
import sys
import os


#Agrego el directorio raiz a la ruta de búsqueda de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from funcionalidad import registrar_log as log

def guardar_directorios(repositorio_imagenes, directorio_collages, directorio_memes, directorio_raiz, usuario):
    """Guarda los directiores relativos de las carpetas y lo carga en el log"""
    data = {'repositorio_imagenes': repositorio_imagenes,
            'directorio_collages': directorio_collages,
            'directorio_memes': directorio_memes}
    with open(os.path.join(directorio_raiz, 'datos', 'configuracion.json'), 'w') as archivo:
        json.dump(data, archivo, indent=4)
        log.registrar_interaccion(usuario, "Cambio en configuración")

    