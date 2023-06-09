import PySimpleGUI as sg
import json
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funcionalidad import registrar_log as log
import rutas as r

def guardar_directorios(repositorio_imagenes, directorio_collages, directorio_memes, directorio_raiz, usuario):
    """Guarda los directiores relativos de las carpetas y lo carga en el log"""
    data = {
        'repositorio_imagenes': os.path.relpath(repositorio_imagenes, directorio_raiz).replace('\\', '/'),
        'directorio_collages': os.path.relpath(directorio_collages, directorio_raiz).replace('\\', '/'),
        'directorio_memes': os.path.relpath(directorio_memes, directorio_raiz).replace('\\', '/')
    }

    with open(r.archivo_configuracion_json, 'w') as archivo:
        json.dump(data, archivo, indent=4)
        log.registrar_interaccion(usuario, "Cambio en configuración")

def obtener_directorios():
    '''Obtengo las rutas del repositorio de imagenes y los directorios, se arma
    la ruta a base de la ruta relativa obtenida del archivo configuracion.json, y
    dependiendo tambien de que sistema operativo se trate'''
    def armar_ruta(directorio,subcarpetas):
        for elem in subcarpetas:
            directorio=os.path.join(directorio,elem)
        return directorio
    try:
        with open(r.archivo_configuracion_json, 'r') as archivo:
            datos=json.load(archivo)
        repositorio_imagenes=armar_ruta(r.directorio_padre,datos['repositorio_imagenes'].split('/'))
        directorio_collages=armar_ruta(r.directorio_padre,datos['directorio_collages'].split('/'))
        directorio_memes=armar_ruta(r.directorio_padre,datos['directorio_memes'].split('/'))
        return repositorio_imagenes,directorio_collages,directorio_memes
    except(FileNotFoundError):
        return None
    except(PermissionError):
        sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'nuevo_perfil.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
        sys.exit()