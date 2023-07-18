import PySimpleGUI as sg
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from rutas import archivo_perfiles_json as ruta_archivo
import rutas as r 

def crear_perfil(values):
    """ Creo el perfil para pasarlo por las diferentes ventanas"""
    
    if values['-GENERO-'][0] != 'Otro':
        genero=values['-GENERO-'][0]
    else: 
        genero=values['-ESPECIFICAR_GENERO-']
    perfil = {
        "Usuario": values["-USUARIO-"],
        "Nombre": values["-NOMBRE-"],
        "Edad": values["-EDAD-"],
        "Genero": genero,
        "Avatar": os.path.basename(values["-BROWSE-"]),
    }
    return perfil

def crear_json(usuario):
    """Le paso el usuario y lo agregar al archivo JSON"""

    datos_agregar = []
    try:
        with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
            datos_agregar = json.load(archivo)
    except PermissionError:
        sg.popup_error("""No se cuentan con los permisos para acceder al archivo 'nuevo_perfil.json', por lo que la aplicacion no puede continuar, se cerrará el programa.""")
        sys.exit()
    except(FileNotFoundError):
        sg.popup("No se encontro el archivo nuevo_perfil.json")
        sys.exit()
    except(json.JSONDecodeError):
        sg.popup("Error fatal: Faltan archivos importante, el programa se cerrará")
        sys.exit()
    
    datos_agregar.append(usuario)
    return datos_agregar

def existe_nombre(alias):
    """Chequea si ya existe el alias en el archivo JSON."""

    try:
        with open(ruta_archivo, "r", encoding="UTF-8") as archivo:
            datos_perfil = json.load(archivo)

        for nombre_usuario in datos_perfil:
            if alias == nombre_usuario["Usuario"]:
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
        values['-BROWSE-'] = r.ruta_imagen_por_defecto
    if values['-GENERO-'] == ['Masculino'] or values['-GENERO-'] == ['Femenino']:
        values['-ESPECIFICAR_GENERO-'] = '-'
