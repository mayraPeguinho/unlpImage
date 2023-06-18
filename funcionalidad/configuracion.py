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
    try:
        with open(r.archivo_configuracion_json, 'w') as archivo:
            json.dump(data, archivo, indent=4)
        log.registrar_interaccion(usuario, "Cambio en configuración")
    except(PermissionError):
        sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'configuracion.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
        sys.exit()

def armar_ruta(directorio,subcarpetas):
    '''Se arma la ruta a partir de la ruta relativa, con las subcarpetas
    '''
    for elem in subcarpetas:
        directorio=os.path.join(directorio,elem)
    return directorio

def obtener_directorio(key):    
    '''Tiene como objetivo obtener y retornar un directorio del archivo de configuración.json.
    key es una cadena de texto que representa la clave que indica la ruta del directorio 
    en el archivo.
    '''
    try:
        with open(r.archivo_configuracion_json, 'r') as archivo:
            datos = json.load(archivo)
        directorio = armar_ruta(r.directorio_padre,datos[key].split('/'))
        return directorio
      
    except(PermissionError):
        sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'configuracion.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
        sys.exit()
    except(FileNotFoundError):
        sg.popup_error("""No se ha encontrado el archivo 'configuracion.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
        sys.exit()
    except json.JSONDecodeError:
        sg.popup_error("""El archivo  configuracion.json no está en formato JSON válido. La aplicación no puede continuar. Se cerrará el programa.""")
        sys.exit()   
    except KeyError as e:
        sg.popup_error(f"Error de clave en el archivo de configuración: {e}. La aplicación no puede continuar. Se cerrará el programa.")
        sys.exit()