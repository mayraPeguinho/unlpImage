import json
import sys
import os


#Agrego el directorio raiz a la ruta de búsqueda de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad import registrar_log as log

def guardar_directorios(repositorio_imagenes, directorio_collages, directorio_memes, directorio_raiz, usuario):
    """Guarda los directiores relativos de las carpetas y lo carga en el log"""
    data = {
        'repositorio_imagenes': os.path.relpath(repositorio_imagenes, directorio_raiz).replace('\\', '/'),
        'directorio_collages': os.path.relpath(directorio_collages, directorio_raiz).replace('\\', '/'),
        'directorio_memes': os.path.relpath(directorio_memes, directorio_raiz).replace('\\', '/')
    }

    with open(os.path.join(directorio_raiz, 'datos', 'configuracion.json'), 'w') as archivo:
        json.dump(data, archivo, indent=4)
        log.registrar_interaccion(usuario, "Cambio en configuración")
    
