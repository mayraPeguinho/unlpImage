import PySimpleGUI as sg
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rutas import archivo_perfiles_json as ruta_archivo
from rutas import ruta_imagenes_perfil

ruta_avatares = os.path.join(ruta_imagenes_perfil, 'avatar.png')

def crear_perfil(values):
    """ Creo el perfil para pasarlo por las diferentes ventanas"""
    
    if values['Genero'] != []:
        genero=values['Genero'][0]
    perfil = {
        "Usuario": values["Usuario"],
        "Nombre": values["Nombre"],
        "Edad": values["Edad"],
        "Genero": genero,
        "Especificar genero": values["Especificar genero"],
        "Avatar": os.path.basename(values["-BROWSE-"]),
    }
    return perfil

def crear_json(usuario):
    """Le paso el usuario y lo agregar al archivo JSON"""

    datos_agregar = []
    try:
        with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
            datos_agregar = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    except PermissionError:
        sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'nuevo_perfil.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
        sys.exit()
    datos_agregar.append(usuario)
    return datos_agregar

def existe_nombre(alias):
    """Chequea si ya existe el alias en el archivo JSON."""

    try:
        with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
            datos_perfil = json.load(archivo)

        for nombre_usuario in datos_perfil:
            if alias in nombre_usuario["Usuario"]:
                return True
    except (FileNotFoundError, json.JSONDecodeError):
        return False
    except PermissionError:
        sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'nuevo_perfil.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
        sys.exit()
    

def verificar_edad(edad):
    """Chequea que la edad ingresada sea un numero entero entre 0-99"""
    try:
        return 99 > int(edad) > 0
    except (TypeError, ValueError):
        return False
    
def llenar_solo(values):
    """Auto completa valores por defecto """
    if values['-BROWSE-'] == '':
        values['-BROWSE-'] = ruta_avatares
    if values['Genero'] == ['Masculino'] or values['Genero'] == ['Femenino']:
        values['Especificar genero'] = '-'
